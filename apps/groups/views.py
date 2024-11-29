from django.shortcuts import render

def home(request):
    return render(request, 'groups/home.html')

def members(request):
    return render(request, 'groups/members.html')
