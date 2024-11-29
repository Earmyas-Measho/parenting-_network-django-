from django.shortcuts import render

def home(request):
    return render(request, 'courses/home.html')

def lessons(request):
    return render(request, 'courses/lessons.html')
