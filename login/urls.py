from django.urls import path
from .views import sign_up,sign_out

urlpatterns = [
    path('register/', sign_up, name='register'),
    path('signout/', sign_out, name='signout'),
]