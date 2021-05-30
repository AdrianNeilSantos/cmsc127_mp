from django.forms import ModelForm
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
