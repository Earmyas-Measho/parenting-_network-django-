from django.shortcuts import render

def home(request):
    return render(request, 'tracking/home.html')

def progress(request):
    return render(request, 'tracking/progress.html')
