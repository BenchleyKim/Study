from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request) :
    return HttpResponse('<html><title>To-Do lists</title></html>')