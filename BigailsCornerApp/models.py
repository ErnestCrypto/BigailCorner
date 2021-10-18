from django.db import models
from django.db.models.deletion import CASCADE




class StockTransaction(models.Model):
    stock_price = models.CharField(max_length=30)
    date_bought = models.DateField()
    
    def __str__(self):
        return self.stock_price + ' : ' + self.date_bought
    
    
    
class Order(models.Model):
    number_of_orders = models.CharField(max_length=10)
    date_ordered = models.DateField()

    def __str__(self):
        return self.number_of_orders + ' : ' + self.date_ordered



class Stock(models.Model):
    stocktransaction = models.OneToOneField(StockTransaction,on_delete=CASCADE)
    number_of_initial_stock = models.CharField(max_length=20)
    date_stock_was_filled = models.DateField()
    number_of_remaining_stock = models.CharField(max_length=20)
    
    def __str__(self):
        return self.number_of_initial_stock  + ' : ' + self.date_stock_was_filled + ' : '+ self.number_of_remaining_stock
        




class Product(models.Model):
    stock = models.OneToOneField(Stock, on_delete=CASCADE)
    total_number_of_products = models.CharField(max_length=20)
    date_products_were_purchased = models.DateField()
    products_left_in_store = models.CharField(max_length=20)
    
    def __str__(self):
        return self.total_number_of_products +' : '+self.date_products_were_purchased +' : ' + self.products_left_in_store 
    
    
    
    
class Orderline(models.Model):
    order = models.ForeignKey(Order,on_delete=CASCADE)
    product = models.OneToOneField(Product, on_delete=CASCADE)
    number_of_orderlines = models.CharField(max_length=10)
    
    def __str__(self):
        return self.product +' : '+ self.number_of_orderlines
    
    
    
    
    
    
