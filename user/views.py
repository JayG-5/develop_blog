from django.shortcuts import render,redirect
from django.views import View
from blog.models import Profile
from .utils.nickname import generate_random_sentence


def social_auth_callback(request):
    return redirect('blog:index')


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            google_social_auth = request.user.social_auth.get()
            print(google_social_auth)
            try:
                user_profile = Profile.objects.get(user=request.user)
                return redirect('blog:index')
            except Profile.DoesNotExist:
                new_nickname = ''
                try:
                    while True:
                        new_nickname = generate_random_sentence()
                        Profile.objects.get(nickname = new_nickname)
                except:
                    new_profile = Profile.objects.create(
                        user=request.user, 
                        nickname=new_nickname,
                    )   
                return redirect('blog:edit',nickname = new_nickname)

        return redirect('blog:index')