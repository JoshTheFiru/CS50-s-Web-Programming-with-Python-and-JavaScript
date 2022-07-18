from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")      #the reason to use the hello/ path is to make sure the file is in the namespace of the project, so it's a needed redundancy of folders. 
                                                    #so when you have many views and apps, you make suer the names won't conflict.
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
