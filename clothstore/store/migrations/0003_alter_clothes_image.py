# Generated by Django 4.1 on 2023-11-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_adminuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(default='/static/images/default.avif', upload_to='store/storage/images'),
        ),
    ]