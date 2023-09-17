from django.shortcuts import render

# Create your views here.

def home(request): 
    return render(request, 'index.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def dynamic(request, id):
    return render(request, 'dynamic.html', {'id':id})