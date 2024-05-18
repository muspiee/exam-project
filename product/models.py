from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(max_length=100)

def __str__(self):
    return self.name