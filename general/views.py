from django.shortcuts import render
from .forms import User


# Create your views here.
def index_page(request):
    response = {}
    return render(request, 'general/index.html', response)


def login(request):
    response = {}
    response['form'] = User()

    return render(request, 'general/login.html', response)
