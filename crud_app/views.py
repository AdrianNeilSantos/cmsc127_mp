import math

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *

# Create your views here.

def home(request):
    pets = Pet.objects.all()
    items = []
    pet_count = 0
    for pet in pets:
        pet_count += 1
        form = WishlistForm({"user": request.user.id, "pet": pet.id})
        items.append({"pet": pet, "form": form})
    data = {
        "items": items,
        "pet_count": pet_count
    }
    return render(request, 'crud_app/pages/home.html', data)


@login_required(login_url='/login')
def cart(request):
    return render(request, 'crud_app/pages/cart.html')

@login_required(login_url='/login')
def addPet(request):
    form = PetForm()
    data = {"form": form}

    if(request.method == 'POST'):
        form = PetForm(request.POST)
        if(form.is_valid):
            form.save()
            # redirect to home
            return redirect("/")

    return render(request, 'crud_app/pages/addPet.html', data)


def pet(request, pk):
    pet = Pet.objects.get(id=pk)
    data = {
        "pet": pet
    }
    return render(request, 'crud_app/pages/pet.html', data)


@login_required(login_url='/login')
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user).order_by('id')
    wishlist = []
    pet_count = 0
    for item in items:
        pet_count = pet_count + 1
        form = WishlistForm({"user": item.user.id, "pet": item.pet.id})
        wishlist.append({"item":item, "form": form})

    data = {"wishlist": wishlist,  "pet_count": pet_count}
    return render(request, 'crud_app/pages/wishlist.html', data)

@login_required(login_url='/login')
def addWishlist(request):
    form = WishlistForm()
    data = {"form": form}

    if(request.method == 'POST'):
        form = WishlistForm(request.POST)
        if(form.is_valid):
            form.save()
            # redirect to home
            return redirect("/wishlist/")

    return render(request, 'crud_app/pages/addWishlist.html', data)


@login_required(login_url='/login')
def deletePet(request, pk):
    pet = Pet.objects.get(id=pk)
    pet.delete()
    return redirect("/")


@login_required(login_url='/login')
def deleteWishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    wishlist.delete()
    return redirect("/wishlist")

def register(request):
    form = UserForm()

    if(request.method == "POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            return redirect('/login')

    data = {"form": form}
    return render(request, 'crud_app/pages/register.html', data)


def login_page(request):
    if( request.method == "POST"):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            print("Login Success.")
            return redirect('/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")
    
    return render(request, 'crud_app/pages/login.html')



def logout_page(request):
    logout(request)
    return redirect('/login/')