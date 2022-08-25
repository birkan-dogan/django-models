from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, welcome</h1>")

def works_include(request):
    return HttpResponse("<h3>Now this response comes")

def second_include(request):
    return HttpResponse("<h3>Now Second response comes</h3>")