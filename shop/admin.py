from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin .ModelAdmin) :
    list_display = ['id' ,'name', 'locality', 'city','user','zipcode','state']

@admin . register (Product)
class ProductModelAdmin(admin .ModelAdmin) :
    list_display = ['id','title', 'MRP','list_price' ,'description', 'brand', 'category','product_image' ]

@admin . register (Cart)
class CartModelAdmin(admin .ModelAdmin) :
    list_display = ['id','user', 'product' ,'quantity']

@admin . register (OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'user','customer', 'product','quantity' ,'order_date' ,'status']