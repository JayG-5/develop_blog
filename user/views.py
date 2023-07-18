from django.shortcuts import render,redirect
from django.views import View
from blog.models import Profile


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
                new_profile = Profile(
                    user=request.user, 
                    nickname=f'{request.user.last_name}{request.user.first_name}',
                    )
                new_profile.save()
        return redirect('blog:index')