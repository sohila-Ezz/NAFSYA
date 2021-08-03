from django.shortcuts import render
from .models import Dates
# Create your views here.
def showdates(request):
    dates=Dates.objects.all()
    return render(request,'dates.html',{'dates':dates})