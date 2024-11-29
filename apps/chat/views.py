from django.shortcuts import render

def home(request):
    return render(request, 'chat/home.html')

def room(request):
    return render(request, 'chat/room.html')
