from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import quandl

data = quandl.get("EIA/PET_RWTC_D", returns="numpy" )
def index(request):
    return HttpResponse(data)