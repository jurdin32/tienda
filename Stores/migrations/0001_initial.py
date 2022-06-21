# Generated by Django 4.0.5 on 2022-06-18 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuarios', '0004_alter_ciudades_options_alter_direcciones_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=120)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.ciudades')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
