from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    prenda_id = models.IntegerField()
    order_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    