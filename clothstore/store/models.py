from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    prenda_id = models.IntegerField()
    order_date = models.DateField()
    payment_method = models.CharField(max_length=50)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='store/templates/images', default='images/default.avif')

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
