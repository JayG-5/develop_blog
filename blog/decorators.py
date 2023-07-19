from django.shortcuts import redirect
from .models import Profile,Post


def check_login(request):
    if request.request.user.is_authenticated:
        return request.request.user
    return redirect('blog:index')

def user_has_permission(required_permissions):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if 'login' in required_permissions:
                redirect_response = check_login(request)
                if type(redirect_response) != type(request.request.user):
                    return redirect_response
            if 'own' in required_permissions:
                owner = Profile.objects.filter(nickname = kwargs.get('nickname',False)).first()
                if not owner:
                    try:
                        post = Post.objects.get(pk=kwargs.get('pk'))
                        owner = post.user
                    except:
                        return redirect('blog:index')
                    post = Post.objects.get(pk = kwargs.get('pk',False))
                    owner = post.user
                if owner:
                    if owner.user != check_login(request):
                        return redirect('blog:index')

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator

    