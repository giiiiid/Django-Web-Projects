from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.log_in, name = 'Signin'),
    path('Signup/', views.sign_up, name = 'Signup')
]