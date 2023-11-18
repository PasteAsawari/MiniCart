from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("This is MyShop Index!")
    return render(request,"myshop/index.html")

def about(request):
    return HttpResponse("This is about page!")

def contact(request):
    return HttpResponse("This is contact page!")

def search(request):
    return HttpResponse("This is search page!")

def tracker(request):
    return HttpResponse("This is tracker page!")

def productView(request):
    return HttpResponse("This is products page!")

def checkout(request):
    return HttpResponse("This is checkout page!")

