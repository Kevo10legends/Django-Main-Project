from django.urls import path


from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact-us',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('gallery',views.gallery,name='gallery'),
    path('my-account',views.my_account,name='my_account'),
    path('shop',views.shop,name='shop'),
    path('shop2',views.shop2,name='shop2'),
    path('wishlist',views.wishlist,name='wishlist'),
]