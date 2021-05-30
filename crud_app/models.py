from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name