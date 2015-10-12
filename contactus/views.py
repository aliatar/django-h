from django.shortcuts import render
from .models import contactus
from .form import contactform
# Create your views here.

def contactview(request):
    form = contactform(request.POST or None)
    if form.is_valid():
        this_form = form.save(commit = False)
        this_form = form.save()

    return render(request , 'contact.html',{
        'form' : form
        })
