from datetime import date
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render , render_to_response
from .models import pro
# Create your views here.

def prov(request):
    products = pro.objects.all()
    return render(request,'products.html',{
        'prod': products

        })
    
def single(request,slug):
    slg = pro.objects.filter(slug=slug)
    return render ( request , 'psingle.html' , {
        'slg' : slg
        })
