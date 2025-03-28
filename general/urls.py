from django.urls import path
from .views import index_page, login, sign_up

urlpatterns = [
    path('', index_page),
    path('login/', login),
    path('registration/', sign_up)
]