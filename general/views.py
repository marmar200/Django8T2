from django.shortcuts import render
from .forms import User, SignUp


# Create your views here.
def index_page(request):
    response = {}
    return render(request, 'general/index.html', response)


def login(request):
    response = {}
    response['form'] = User()

    return render(request, 'general/login.html', response)


def sign_up(request):
    response = {}
    response['form'] = SignUp()
    return render(request, 'general/sign_up.html', response)
