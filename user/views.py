from django.shortcuts import render,redirect
from django.views import View
from blog.models import Profile as profile


def social_auth_callback(request):
    return redirect('blog:index')


class Profile(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            google_social_auth = request.user.social_auth.get(provider='google-oauth2')
            user_profile = profile.objects.get(user=request.user)
            if not user_profile:
                new_profile = Profile(user=request.user, name=request.user.username)
                new_profile.save()
        redirect('blog:index')