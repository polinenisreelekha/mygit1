from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sree(request):
    return HttpResponse('<marquee><h2>hi sree</marquee></h2>')
def jessy(request):
    return HttpResponse('<marquee><h2>hi jessy</marquee></h2>')    