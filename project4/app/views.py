from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def sree(request):
    return HttpResponse('<marquee>hi sree</marquee>')