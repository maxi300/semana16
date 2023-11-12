# Generated by Django 4.2.6 on 2023-11-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_alter_clientes_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='tfno',
            field=models.CharField(max_length=8, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='direccion',
            field=models.DateField(verbose_name='fecha'),
        ),
    ]