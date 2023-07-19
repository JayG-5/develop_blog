from django.urls import path
from .views import Index,DetailView,WriteView,UserView,EditProfileView,PostDelete,UpdateView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("detail/<int:pk>/", DetailView.as_view(), name='detail'),
    path("update/<int:pk>/", UpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", PostDelete.as_view(), name='delete'),
    path("write/", WriteView.as_view(), name='write'),
    path("@<str:nickname>/", UserView.as_view(), name='user'),
    path("@<str:nickname>/edit/", EditProfileView.as_view(), name='edit'),
]