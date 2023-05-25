from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),  # 회원가입하기
    path("login/", views.AuthView.as_view()),  # 로그인하기
    path('login/refresh/', TokenRefreshView.as_view()),  # 토큰 재발급하기
]
