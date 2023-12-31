from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username']
        # fields = UserCreationForm.Meta.fields + ('email',)


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        # }