from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    prenda_id = models.IntegerField()
    order_date = models.DateField()
    payment_method = models.CharField(max_length=50)

class Prenda(models.Model):
    prenda_id = models.AutoField(primary_key=True)
    prenda_category = models.CharField(max_length=50)
    prenda_price = models.IntegerField()
    prenda_color = models.CharField(max_length=50)
    prenda_size = models.CharField(max_length=50)
    prenda_description = models.CharField(max_length=50)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_payment_method = models.CharField(max_length=50)
