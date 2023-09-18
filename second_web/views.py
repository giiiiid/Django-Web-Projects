from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from email.message import EmailMessage
from django.http import HttpResponse
from .models import NewServices, Blogs
# import ssl
# import smtplib
# from .forms import ContactForm

# Create your views here.
def homepage(request):
    new_servs = NewServices.objects.all()
    # servs = Services.objects.all()
    # serv1 = Services()
    # serv1.name = 'Determination'
    # serv1.details = 'We focus on nurturing your business to be the best fit the creative and digital world.'
    # serv1.is_true = True

    # serv2 = Services()
    # serv2.name = 'Customer Segment'
    # serv2.details = 'Our business clients are our number 1 priority.'
    # serv2.is_true = True

    # serv3 = Services()
    # serv3.name = 'Creative'
    # serv3.details = 'With our talented team, we can achieve anything in the creative world.'
    # serv3.is_true = True

    # serv4 =  Services()
    # serv4.name = 'Partnership'
    # serv4.details = 'Your business grows, ours too grow.'
    # serv4.is_true = False

    # all_services = [serv1, serv2, serv3, serv4]
    # return render(request, 'home.html', {'serv1':serv1, 'serv2':serv2, 'serv3':serv3, 'serv4':serv4})
    return render(request, 'home.html', {'new_servs':new_servs})

def details(request, id):
    new_servs = NewServices.objects.get(id=id)
    return render(request, 'details.html', {'new_servs':new_servs})

def blog_page(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})

def singles(request, id):
    Blogsingles = Blogs.objects.get(id=id)
    return render(request, 'blog-single.html', {'Blogsingles':Blogsingles})

def portfolio(request):
    return render(request, 'portfolio-details2.html')

def register(request):
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
    #     return redirect('register')
        return render(request, 'register.html')

def login(request):
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

def logout(request):
    auth.logout(request)
    return redirect('login')

def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = request.POST.get('subject')

    # em = EmailMessage(
    #     subject = f'{name} from Tempo',
    #     body=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     to_email=settings.EMAIL_HOST_USER,
    #     reply_to = [email]
    # )      
    # email.send()
    # return HttpResponse('Success')
    form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
    }
    message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
    send_mail('You got a mail!', message, '', [settings.EMAIL_HOST_USER])

    return render(request, 'home.html',{})
    
def success(request):
    return render(request, 'success.html')

