# Generated by Django 2.0.9 on 2018-10-14 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_stock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock',
            new_name='StockLevel',
        ),
    ]