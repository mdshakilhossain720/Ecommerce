from django.contrib import admin
from .models import (
    Product,
    Cart,
    Customer,
    OrderPlace,
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','division','dis','thana','village','zipcode']

@admin.register(Product)
class ProductMOdelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_prices','discount','description','brand','categroy','product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(OrderPlace)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','status']

