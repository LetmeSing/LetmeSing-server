import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from django.views.decorators.http import require_http_methods
from albums.models import Music
from django.http import JsonResponse
import os
import json
import random

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


client_id = get_secret("client_id")
client_secret = get_secret("client_secret")


client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@require_http_methods(["GET"])
def get_recommendations(request):

    music = Music.objects.all()
    artist_name = []
    track_name = []
    artist_id = []
    track_id = []
    for _ in range(2):
        idx = random.randrange(len(music))
        artist_name.append(music[idx].singer)
        track_name.append(music[idx].name)

    tmp_dict = {}
    for i in range(2):
        tmp_dict[artist_name[i]] = track_name[i]

    for artist, song in tmp_dict.items():
        tmp = artist + " " + song
        track_results = sp.search(q=tmp, type='track', market='KR', limit=1)
        artist_id.append(track_results['tracks']
                         ['items'][0]['artists'][0]['id'])
        track_id.append(track_results['tracks']['items'][0]['id'])

    rec = sp.recommendations(seed_artists=artist_id, seed_genres=[
                             "korean pop"], seed_tracks=track_id, limit=10, market="KR")

    recom_all = []
    for track in rec['tracks']:
        recom = {
            "artist": track['artists'][0]['name'],
            "track": track["name"],
            "image": track['album']['images'][2]['url']
        }
        recom_all.append(recom)

    return JsonResponse({
        'status': 200,
        'message': '음악 추천 성공',
        'data': recom_all
    })
