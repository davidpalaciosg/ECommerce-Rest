from django.db import models
from apps.shared.models import SharedModelHistorical

# Create your models here.

#Measure Unit Model
class MeasureUnit(SharedModelHistorical):

    description = models.CharField('Descripción', max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.description

#Category Product Model  
class CategoryProduct(SharedModelHistorical):

    description = models.CharField('Descripción', max_length=50, null=False, blank=False, unique=True)
    
    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    def __str__(self):
        return self.description

#Discount Indicator Model
class Indicator(SharedModelHistorical):

    discount_value = models.PositiveSmallIntegerField('Valor de Descuento', default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto')
    
    class Meta:
        verbose_name = "Indicador de Descuento"
        verbose_name_plural = "Indicadores de Descuento"

    def __str__(self):
        return f'Oferta de la categoría {self.category_product}: {self.discount_value}%'

#Product Model
class Product(SharedModelHistorical):
    
    name = models.CharField('Nombre de Producto', max_length=150, null=False, blank=False, unique=True)
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Imagen de Producto', upload_to='products/', null=True, blank=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, null=True, blank=False, verbose_name='Unidad de Medida')
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name