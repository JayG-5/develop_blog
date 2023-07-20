from django.urls import path
from .views import social_auth_callback,ProfileView
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('social-auth-callback/', social_auth_callback, name='social_auth_callback'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]