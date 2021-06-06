from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request) :
    if request.method == 'POST' :
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')