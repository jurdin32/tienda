# Generated by Django 4.0.5 on 2022-06-14 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_remove_perfiles_ciudad_remove_perfiles_direccion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudades',
            options={'verbose_name_plural': '2. Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='direcciones',
            options={'verbose_name_plural': '4. Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='perfiles',
            options={'verbose_name_plural': '3. Perfiles'},
        ),
        migrations.AlterModelOptions(
            name='provincias',
            options={'verbose_name_plural': '1. Provincias'},
        ),
    ]
