from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'crud_app/pages/home.html')

def signIn(request):
    return render(request, 'crud_app/pages/signIn.html')

def signUp(request):
    return render(request, 'crud_app/pages/signUp.html')

def wishlist(request):
    return render(request, 'crud_app/pages/wishlist.html')

def cart(request):
    return render(request, 'crud_app/pages/cart.html')
