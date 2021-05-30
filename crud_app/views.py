from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    pets = Pet.objects.all()

    data = {
        "pets": pets,
    }
    return render(request, 'crud_app/pages/home.html', data)

def signIn(request):
    return render(request, 'crud_app/pages/signIn.html')

def signUp(request):
    return render(request, 'crud_app/pages/signUp.html')

def wishlist(request):
    return render(request, 'crud_app/pages/wishlist.html')

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
