from django.contrib import admin
from .models import * 

class CategotyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')



class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'text', 'rating', 'created_at')    



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)








