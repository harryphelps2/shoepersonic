# Generated by Django 2.0.9 on 2018-10-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181025_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklevel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
