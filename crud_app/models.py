from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=10, null=True)
    picture = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)