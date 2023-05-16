from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.AlbumViewSet)
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
