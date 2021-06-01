from django.shortcuts import render, redirect
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

def signIn(request):
    return render(request, 'crud_app/pages/signIn.html')

def signUp(request):
    return render(request, 'crud_app/pages/signUp.html')


def cart(request):
    return render(request, 'crud_app/pages/cart.html')

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

def deletePet(request, pk):
    pet = Pet.objects.get(id=pk)
    pet.delete()
    return redirect("/")

def deleteWishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    wishlist.delete()
    return redirect("/wishlist")