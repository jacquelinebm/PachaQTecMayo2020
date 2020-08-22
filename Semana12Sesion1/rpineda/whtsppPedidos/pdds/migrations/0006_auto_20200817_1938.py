# Generated by Django 3.1 on 2020-08-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdds', '0005_auto_20200817_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipocliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipocliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipodocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipodocumento'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.cliente'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipoproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipoproducto'),
        ),
        migrations.AlterField(
            model_name='transportista',
            name='tipoDocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipodocumento'),
        ),
    ]