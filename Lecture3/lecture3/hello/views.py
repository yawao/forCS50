from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# The argument of request is a request that user made in order to access the web server
def index(request):
    return render(request, "hello/index.html")

def yuki(request):
    return HttpResponse("Hello Yuki!")

def asai(request):
    return HttpResponse("Hello Asai!")

def greet(request, name):
    return render(request, "hello.greet.html", {
        "name": name.capitalize()
    })