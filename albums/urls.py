from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.AlbumViewSet)

urlpatterns = [
    path('/album/', include(router.urls))
]
