from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('blogs/', views.blog_page, name = 'blogpage'),
    path('blogpage/<str:id>', views.singles, name = 'single'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('signup/', views.register, name = 'register'),
    path('signin/', views.login, name = 'login'),
    path('success/', views.success, name='success'),
    path('logout/', views.logout, name='logout'),
    path('details/<str:id>', views.details, name='details'),
    path('contact/', views.send_email, name='contact')
]