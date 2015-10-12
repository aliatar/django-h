from django.shortcuts import render
from .models import cart
from django.http import HttpResponseRedirect
from pro.models import pro
# Create your views here.

def cartview(request):
    return render(request , 'cart.html')

def add(request, slug):
    p = pro.objects.get(slug=slug)
    request.session.set_expiry(30)

    try:
        active = request.session['cart']
    except:
        request.session['cart'] = 'empty'

    if request.session != 'empty':
        cart = request.session['cart']
        update_cart = cart.objects.get(id=cart)
        update_cart.product.add(p)
        update_cart.save()
        request.session['total_item'] = len(pro.objects.all())

    else:
        new_cart = cart()
        new_cart.save()
        new_cart.product.add(p)
        request.session['cart'] = cart.id
        request.session['cart'] = len(pro.objects.all())

    return HttpResponseRedirect('/pro/%s'%(slug))

