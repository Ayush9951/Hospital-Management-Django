from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def hospital(request):
    return render(request, 'hospital/hospital.html')
