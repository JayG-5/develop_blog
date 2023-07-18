from django.shortcuts import redirect
from .models import Profile


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
                owner = Profile.objects.get(nickname = kwargs.get('nickname'))
                if owner.user != check_login(request):
                    return redirect('blog:index')

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator

    