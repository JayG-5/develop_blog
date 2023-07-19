from django import forms
from .models import Profile,Image

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','bio']
        
        labels = {
            'nickname': '닉네임',
            'bio': '자기소개',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': '3', 'cols':'35'})
        }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        
        labels = {
            'image': '프로필 이미지',
        }
