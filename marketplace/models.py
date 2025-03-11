from django.db import models
from django.contrib.auth.models import AbstractUser



class Item(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True, default='images/default.jpg')
    n = models.IntegerField()


class User(AbstractUser):
    pass


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    items = models.ManyToManyField(Item, related_name="carts")
    