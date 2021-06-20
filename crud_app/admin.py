from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Pet)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(OwnedPet)
admin.site.register(AdopterRequest)
admin.site.register(AdopteeRequest)