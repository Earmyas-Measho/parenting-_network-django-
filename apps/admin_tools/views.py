from django.shortcuts import render

def dashboard(request):
    return render(request, 'admin_tools/dashboard.html')

def reports(request):
    return render(request, 'admin_tools/reports.html')
