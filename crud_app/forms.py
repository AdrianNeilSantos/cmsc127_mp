from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 
from .models import * 

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"
        # fields = ["name", "student_number"]
        # labels = {
        #     "name": "Ilagay ang Pangalan",
        #     "student_number": "Ilagay ang Student number"
        # }

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"
        widgets = {
            'user':  HiddenInput( attrs = {'type':'hidden'} ),
            'pet':  HiddenInput( attrs = {'type':'hidden'} ),
        }