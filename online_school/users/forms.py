from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль' ,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))