from django import forms


class User(forms.Form):
    login = forms.CharField(label='ЛОГИН', max_length=32)
    password = forms.CharField(label='ПАРОЛЬ', max_length=64)
