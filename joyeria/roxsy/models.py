from django.db import models

# Create your models here.
class Producto(models.Model):
    CATEGORIA_PULSERA= 'PULSERA'
    CATEGORIA_COLLAR= 'COLLAR'
    CATEGORIA_ARETE= 'ARETE'
    CATEGORIAS_CHOICES=[
        (CATEGORIA_PULSERA, 'PULSERA'), (CATEGORIA_COLLAR, 'COLLAR'), (CATEGORIA_ARETE, 'ARETE')
    ]
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="Images/")
    categoria = models.CharField(max_length=10, choices=CATEGORIAS_CHOICES, null=True, blank=True)

    def __str__(self):
        return (self.nombre)
    