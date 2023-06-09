from django.db import models
from django.contrib.auth.models import User
import datetime


    
class Customer(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
   name = models.CharField(max_length=200, null=True)
   email = models.EmailField(max_length=200, null=True)
   # address = models.CharField (max_length=100, default='', blank=True)
    # phone = models.CharField (max_length=100, default='', blank=True)

   def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    price= models.FloatField()
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    digital = models. BooleanField(default=False, null=True, blank=False)
    image= models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
 
class Order(models.Model):
    # product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField (auto_now_add=True)
    complete = models.BooleanField (default=False , null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.id)
     

    @property
    def get_cart_total(self):
        Orderitems = self.ordertitem_set.all()
        total = sum([item.get_total for item in Orderitems])
        return total
    
   

class Orderitems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    order =  models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField (auto_now_add=True)
    

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total