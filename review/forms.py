from django import forms
from review.models import Credentials

class CredentialsForm(forms.ModelForm):

    username = forms.CharField(max_length=128, help_text="Enter your Username")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter your Private Key")

    class Meta:
        model = Credentials
        #fields = (username,password)
    

#class SignupForm(forms.ModelForm):
#    Name