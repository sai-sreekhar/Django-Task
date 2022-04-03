from django.shortcuts import render
from sympy import false
from urllib3 import HTTPResponse
from django.http import HttpResponse

from travello.models import Destination

# Create your views here.

def index(request):
    
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

