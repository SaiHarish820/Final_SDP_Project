# Generated by Django 4.1.1 on 2022-12-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidbro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_img',
            new_name='product_img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
