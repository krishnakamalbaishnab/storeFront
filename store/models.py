from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now = True)

class Customer(models.Model):
    firstName = models.CharField(255)
    lastName = models.CharField(255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birthData = models.DateTimeField(null=True)



