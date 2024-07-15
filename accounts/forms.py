from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='User Name', max_length=11)

    def clean(self):
        user = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if user and password:
            self.user_cache = authenticate(self.request, username=user, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Login inválido. Por favor, tente novamente.')
        return self.cleaned_data
