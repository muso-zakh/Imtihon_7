from django.urls import path, include
from .views import register_api, profile, CustomAuthToken, change_password, LogoutAPIView


urlpatterns = [
    path('register/', register_api, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('change-password/', change_password),
    path('logout', LogoutAPIView.as_view())

]  