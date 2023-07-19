from django.urls import path
from .views import Index,DetailView,WriteView,UserView,EditProfileView,PostDelete,UpdateView,UserFollow,PostLike

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("detail/<int:pk>/", DetailView.as_view(), name='detail'),
    path("detail/<int:pk>/like/", PostLike.as_view(), name='like'),
    path("update/<int:pk>/", UpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", PostDelete.as_view(), name='delete'),
    path("write/", WriteView.as_view(), name='write'),
    path("@<str:nickname>/", UserView.as_view(), name='user'),
    path("@<str:nickname>/edit/", EditProfileView.as_view(), name='edit'),
    path("@<str:nickname>/follow/", UserFollow.as_view(), name='follow'),
]