# Generated by Django 4.0.5 on 2022-06-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0010_categorias_productos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='porciones',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productos',
            name='tamanio',
            field=models.CharField(default='Pequeño', max_length=30),
        ),
    ]