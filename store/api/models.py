from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from rest_framework.response import Response
from .serializers import *

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
 
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Order {self.pk}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
 
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

def __str__(self):
    return f"Cart for {self.user.username}"



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

def __str__(self):
    return f"{self.cart.user.username} - {self.product.name} - Quantity: {self.quantity}"



class ClientUser(AbstractBaseUser):
    email = models.EmailField(unaque=True)


    def __str__(self):
        return self.username



class Client(models.Model):
    user = models.OneToOneField(ClientUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.user.username




















