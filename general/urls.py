from django.urls import path
from .views import index_page, login

urlpatterns = [
    path('', index_page),
    path('login/', login)
]