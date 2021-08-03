from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showarconsulation(request):
    return HttpResponse("this is my consulation")