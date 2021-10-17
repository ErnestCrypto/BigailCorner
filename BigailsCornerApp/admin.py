from django.contrib import admin
from .models import Product,Order,Orderline,Stock,StockTransaction

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderline)
admin.site.register(Stock)
admin.site.register(StockTransaction)