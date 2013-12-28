from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def archive(request):
    
    return HttpResponse('The archive!')
    
def home(request):
    
    return HttpResponse('Home Page!')