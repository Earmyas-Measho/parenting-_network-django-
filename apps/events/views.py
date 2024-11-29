from django.shortcuts import render

def home(request):
    return render(request, 'events/home.html')

def calendar(request):
    return render(request, 'events/calendar.html')
