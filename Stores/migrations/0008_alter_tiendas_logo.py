# Generated by Django 4.0.5 on 2022-06-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0007_tiendas_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiendas',
            name='logo',
            field=models.ImageField(default='tienda_mia.png', upload_to='logos'),
        ),
    ]
