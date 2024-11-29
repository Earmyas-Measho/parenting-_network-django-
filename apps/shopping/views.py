from django.shortcuts import render

def home(request):
    return render(request, 'shopping/home.html')

def products(request):
    return render(request, 'shopping/products.html')
