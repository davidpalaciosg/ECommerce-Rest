# Generated by Django 4.1.3 on 2022-12-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_historicalproduct_historicalmeasureunit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto', 'verbose_name_plural': 'historical Productos'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
