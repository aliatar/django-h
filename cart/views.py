from django.shortcuts import render, get_object_or_404
from .models import Cart
from django.http import HttpResponseRedirect
from pro.models import pro
# Create your views here.

def add(request, slug):
    p = pro.objects.get(slug=slug)
    request.session.set_expiry(30)

    try:
        active = request.session['cart']
    except:
        request.session['cart'] = 'Empty'

    if request.session['cart'] != 'Empty':
        cart = request.session['cart']
        update_cart = Cart.objects.get(id=cart)
        update_cart.pro.add(p)
        update_cart.save()
        request.session['total_item'] = len(pro.objects.all())

    else:
        new_cart = Cart()
        new_cart.save()
        new_cart.product.add(p)
        request.session['cart'] = new_cart.id
        request.session['cart'] = len(pro.objects.all())

    return HttpResponseRedirect('/pro/%s'%(slug))

def cartview(request):
    try:
        cart_id = request.session['cart']
        cart_exist = Cart.objects.get(id=cart_id)
    except:
        cart_exist = False
    return render(request , 'cart.html',{
        'cart_exist' : cart_exist
        })


