from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.core import mail
from django.conf import settings
from email.message import EmailMessage
from django.http import HttpResponse
from .models import NewServices, Blogs


# Create your views here.

def homepage(request):       # View for the homepage
    new_servs = NewServices.objects.all()
    
    return render(request, 'home.html', {'new_servs':new_servs})

def detailed_services(request, id):      # View to read more about our services
    new_servs = NewServices.objects.get(id=id)
    return render(request, 'details.html', {'new_servs':new_servs})

def blog_page(request):        # View to showcase blogs
    blogs = Blogs.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})

def singles(request, id):      # View to read a specific blog
    Blogsingles = Blogs.objects.get(id=id)
    return render(request, 'blog-single.html', {'Blogsingles':Blogsingles})

def portfolio(request):        # View to show the portfolio of each element
    return render(request, 'portfolio-details2.html')

def register(request):         # Registration to access Tempo
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password  = request.POST['password1']
        password1 = request.POST['password2']

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Been Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):            # Login
    if request.method == 'POST':
        username = request.POST['username']
        passed = request.POST['password1']
        user = auth.authenticate(username = username, password= passed)
        if user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('homepage')
    else:
        return render(request, 'login.html')

def logout(request):              # Logout
    auth.logout(request)
    return redirect('login')

def contact(request):             # Sending emails
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = request.POST.get('subject')
    send_mail(subject, message, email, [settings.EMAIL_HOST_USER])


    #-----------Another method-------------#
    # with mail.get_connection() as connection:
    #     mail.EmailMessage(
    #         subject,
    #         message,
    #         email,
    #         [settings.EMAIL_HOST_USER],
    #         connection=connection,
    #     ).send()
    return render(request, 'contact.html')



