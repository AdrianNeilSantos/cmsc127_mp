from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 
from .models import * 
from django import forms


SEX_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),

]

PET_TYPE = [
    ('cat', 'Cat'),
    {'dog', 'Dog'},
    ('bird', 'Bird'),
    ('rabbit', 'Rabbit'),
    ('fish', 'Fish'),
    ('others', 'Ohers')
]




class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"
        # fields = ["name", "student_number"]
        labels = {
            'owner':  HiddenInput( attrs = {'type':'hidden'} ),
        }
        widgets = {
            'sex' : forms.Select(choices=SEX_CHOICES),
            'petType': forms.Select(choices=PET_TYPE)
        }


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }


class OwnedPetForm(ModelForm):
    class Meta:
        model = OwnedPet
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }


class AdopterRequestForm(ModelForm):
    class Meta:
        model = AdopterRequest
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }


class AdopteeRequestForm(ModelForm):
    class Meta:
        model = AdopteeRequest
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }



class UserForm(UserCreationForm):
    attrs = { 'class': 'input', 'type':'password'} 
    password1 =  CharField( widget=PasswordInput(attrs=attrs) )
    password2 =  CharField( widget=PasswordInput(attrs=attrs) )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = { 
            'username': TextInput( attrs={ 'class': 'input'} ),
            'email': TextInput( attrs={ 'class': 'input', 'type':'email'} ),
        }