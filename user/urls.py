from django.urls import path
from .views import Login,Registration
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reg/', Registration.as_view(), name='reg'),
    path('login/', Login.as_view(), name='login'),
]