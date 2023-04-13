from django.contrib import admin
from .models import Products,  Order, Orderitems, Customer

# Register your models here.
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderitems)