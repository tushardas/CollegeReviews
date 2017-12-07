from django import forms
from review.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    #username = forms.CharField(max_length=128, help_text="Enter your Username")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter your Private Key")

    class Meta:
        model = User
        fields = ('username','password')
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
