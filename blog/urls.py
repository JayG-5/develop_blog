from django.urls import path
from .views import Index,DetailView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("detail/<int:pk>/", DetailView.as_view(), name='detail'), # /blog/detail/1
]