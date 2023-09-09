# Generated by Django 4.1.5 on 2023-09-09 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prenda',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_payment_method',
            new_name='payment_method',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prenda_size',
            new_name='size',
        ),
    ]