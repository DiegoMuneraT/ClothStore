from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings  # To link the default User model

class Clothes(models.Model):
    class Size(models.TextChoices):
        S = 'S', _('S')
        M = 'M', _('M')
        L = 'L', _('L')
        XL = 'XL', _('XL')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=2, choices=Size.choices, default=Size.S)
    description = models.TextField()
    image = models.ImageField(upload_to='store/templates/images', default='images/default.avif')

class CreditCard(models.Model):
    class CardType(models.TextChoices):
        VISA = 'VS', _('Visa')
        MASTER = 'MC', _('MasterCard')
        # Add more if needed

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='credit_cards')
    cardholder_name = models.CharField(max_length=255)
    expiry_date = models.DateField()
    last_four_digits = models.CharField(max_length=4)
    card_type = models.CharField(max_length=2, choices=CardType.choices, default=CardType.VISA)
    is_default = models.BooleanField(default=False)

class Order(models.Model):
    class ShippingStatus(models.TextChoices):
        CART = 'CA', _('Cart')
        PLACED = 'PL', _('Placed')
        SHIPPED = 'SH', _('Shipped')
        DELIVERED = 'DL',_('Delivered')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0,)
    status = models.CharField(max_length=2, choices=ShippingStatus.choices, default=ShippingStatus.PLACED)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.SET_NULL, null=True, related_name='used_in_orders')
    items = models.ManyToManyField(Clothes, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_info')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=100)

class Review(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # You can use validators to restrict it to a range like 1-5.
    comment = models.TextField()
