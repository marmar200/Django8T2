from django import forms


class User(forms.Form):
    login = forms.CharField(label='ЛОГИН', max_length=32)
    password = forms.CharField(label='ПАРОЛЬ', max_length=64)

class SignUp(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Иван',
                'type': 'text',
                'class': 'form-control'
            }) 
        )
    
    surname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Иванов',
                'type': 'text',
                'class': 'form-control'
            }) 
        )
    
    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ypur@example.ru',
                'type': 'email',
                'class': 'form-control'
            }) 
        )

    password = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Пароль',
                'type': 'password',
                'class': 'form-control'
            }) 
        )
    
    confirm_password = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Подтвердите пароль',
                'type': 'password',
                'class': 'form-control'
            }) 
        )
    