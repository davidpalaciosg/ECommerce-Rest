# Generated by Django 4.1.3 on 2023-01-05 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_categoryproduct_measure_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoria de Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
            preserve_default=False,
        ),
    ]
