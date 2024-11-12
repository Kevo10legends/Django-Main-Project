from urllib import request

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact-us.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def gallery(request):
    return render(request,'gallery.html')

def my_account(request):
    return render(request,'my-account.html')

def shop(request):
    return render(request,'shop.html')

def shop2(request):
    return render(request,'shop_detail.html')

def wishlist(request):
    return render(request,'wishlist.html')

def base(request):
    return render(request,'base.html')
