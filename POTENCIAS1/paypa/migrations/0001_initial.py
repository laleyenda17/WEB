# Generated by Django 4.0 on 2022-01-02 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=100)),
                ('codigo_estado', models.CharField(max_length=100)),
                ('total_de_la_compra', models.DecimalField(decimal_places=3, max_digits=6)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('correo_cliente', models.EmailField(max_length=100)),
                ('direccion_cliente', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paypa.producto')),
            ],
        ),
    ]
