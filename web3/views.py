from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        used = request.POST['email']
        passes = request.POST['password1']

        user = auth.authenticate(email=used, password=passes)
        
        if user is None:
            messages.info(request, 'User does not exist')
        else:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')
    return render(request, 'form1.html')
    #     if passes == passes:
    #         if User.objects.filter(email=used).exists():
    #             return HttpResponse('Hi')
    #         else:
    #             messages.info(request, 'Invalid email')
    #     else:
    #         messages.info(request, 'Incorrect Password')
    # else:
    #     return render(request, 'form1.html')

def sign_up(request):
    new = False
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username = username).exists():
            messages.info(request, 'Account with username already exists')
            return redirect('Signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Account with email already exists')
            return redirect('Signup')
        else:
            new = True
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            messages.info(request, 'Account created, login to access your dashboard')
            return redirect('Signin')
    return render(request, 'form1.html')
