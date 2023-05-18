from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', views.AlbumList.as_view()),
    path('<int:pk>/', views.AlbumDetail.as_view()),
    path('music/', views.MusicList.as_view()),
    path('music/<int:pk>/', views.MusicDetail.as_view()),
]
