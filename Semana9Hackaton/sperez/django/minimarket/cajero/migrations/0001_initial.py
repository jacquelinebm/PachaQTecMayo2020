# Generated by Django 3.0.8 on 2020-07-27 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('e', 'efectivo'), ('t', 'tarjeta')], max_length=1)),
                ('cantidad', models.IntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('ruc_dni', models.BigIntegerField(verbose_name='ruc_dni')),
                ('fecha', models.DateField()),
                ('igv', models.DecimalField(decimal_places=3, max_digits=3)),
                ('monto_pagar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.Producto')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.venta')),
            ],
        ),
    ]
