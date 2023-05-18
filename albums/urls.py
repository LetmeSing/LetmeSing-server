from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view()),
    path('<int:pk>/', views.AlbumDetail.as_view()),
    path('music/', views.MusicList.as_view()),
    path('music/<int:pk>/', views.MusicDetail.as_view()),
]
