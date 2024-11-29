from django.shortcuts import render

def home(request):
    return render(request, 'notifications/home.html')

def alerts(request):
    return render(request, 'notifications/alerts.html')
