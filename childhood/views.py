from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def startegies(request):
    return render(request,"key startegies.html")

def goals(request):
    return render(request,"goals.html")

def position(request):
    return render(request,"position.html")

def role(request):
    return render(request,"role.html")

def references(request):
    return render(request,"references.html")