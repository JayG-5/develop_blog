from django.urls import path
from .views import Index,DetailView,WriteView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("detail/<int:pk>/", DetailView.as_view(), name='detail'),
    path("write/", WriteView.as_view(), name='write'),
]