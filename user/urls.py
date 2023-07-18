from django.urls import path
from .views import social_auth_callback,ProfileView

app_name = 'user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('social-auth-callback/', social_auth_callback, name='social_auth_callback'),
]