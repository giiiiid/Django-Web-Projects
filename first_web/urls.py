from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.inner_page),
    path('port/', views.portfolio, name = 'port'),
    path('post/<str:id>', views.dynamic, name='dynamic')
]