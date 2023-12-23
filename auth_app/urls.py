from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, CurrentUserAPIView

name = 'auth_app'
urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('current_user/', CurrentUserAPIView.as_view(), name='current_user')
]
