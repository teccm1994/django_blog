from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))