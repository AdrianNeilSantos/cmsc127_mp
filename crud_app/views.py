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
def cart(request):
    items = Cart.objects.filter(user=request.user).order_by('id')
    cart = []
    pet_count = 0
    for item in items:
        pet_count = pet_count + 1
        form = CartForm({"user": item.user.id, "pet": item.pet.id})
        cart.append({"item":item, "form": form})

    data = {"cart": cart,  "pet_count": pet_count}
    return render(request, 'crud_app/pages/cart.html', data)



@login_required(login_url='/login')
def requestPet(request):
    items = Cart.objects.filter(user=request.user)
    #Implement code that will transfer pet to requests 

    for item in items:
        adoptee = AdopteeRequest(user = request.user, pet=item.pet, date_created=item.date_created)
        adopter = AdopterRequest(user = item.pet.owner, pet=item.pet, date_created=item.date_created)

        adoptee.save()
        adopter.save()


    Cart.objects.filter(user=request.user).delete()
    return redirect("/requests")



@login_required(login_url='/login')
def profile(request):
    items = OwnedPet.objects.filter(user=request.user).order_by('id')
    ownedPet = []
    pet_count = 0
    for item in items:
        pet_count += 1
        form = OwnedPetForm({"user": item.user.id, "pet": item.pet.id})
        ownedPet.append({"item":item, "form": form})

    data = {"ownedPet": ownedPet,  "pet_count": pet_count, "user": request.user}

    return render(request, 'crud_app/pages/profile.html', data)


@login_required(login_url='/login')
def requests(request):
    adopterItems = AdopterRequest.objects.filter(user=request.user).order_by('id')
    adopteeItems = AdopteeRequest.objects.filter(user=request.user).order_by('id')
    adopterRequest = []
    adopteeRequest = []

    adopter_count = 0
    adoptee_count = 0

    for item in adopterItems:
        adopter_count += 1
        form = AdopterRequestForm({"user": item.user.id, "pet": item.pet.id})
        adopterRequest.append({"item":item, "form": form})

    for item in adopteeItems:
        adoptee_count += 1
        form = AdopteeRequestForm({"user": item.user.id, "pet": item.pet.id})
        adopteeRequest.append({"item":item, "form": form})

    data = {"adopterRequest": adopterRequest, "adopteeRequest": adopteeRequest,
              "adopter_count": adopter_count, "adoptee_count": adoptee_count, "user": request.user}

    return render(request, 'crud_app/pages/requests.html', data)



@login_required(login_url='/login')
def addWishlist(request):
    form = WishlistForm()
    data = {"form": form}

    if(request.method == 'POST'):
        form = WishlistForm(request.POST)
        if(form.is_valid()):
            cleaned_info = form.cleaned_data
            num_results = Wishlist.objects.filter(user=request.user, pet=cleaned_info['pet']).count()
            if(num_results == 0):
                form.save()
            # redirect to home
            return redirect("/wishlist/")

    return render(request, 'crud_app/pages/addWishlist.html', data)

@login_required(login_url='/login')
def addCart(request):
    form = CartForm()
    data = {"form": form}

    if(request.method == 'POST'):
        form = CartForm(request.POST)
        if(form.is_valid()):
            cleaned_info = form.cleaned_data
            num_results = Cart.objects.filter(user=request.user, pet=cleaned_info['pet']).count()
            if(num_results == 0):
                form.save()
            # redirect to home
            return redirect("/cart/")

    return render(request, 'crud_app/pages/addCart.html', data)




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

@login_required(login_url='/login')
def deleteCart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return redirect("/cart")


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