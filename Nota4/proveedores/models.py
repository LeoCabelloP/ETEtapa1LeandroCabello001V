from django.db import models

# Create your models here.

class Usuario(models.Model):
    numId = models.CharField(primary_key=True, max_length=10,  verbose_name='Número de indentificación')
    logoProveedor = models.ImageField(upload_to='photos', null=True, blank=True, verbose_name='Logo del proveedor')
    nombre = models.CharField(max_length=10, verbose_name='Nombre de proveedor')
    fono = models.CharField(max_length=12, verbose_name='Número de teléfono')
    direccion = models.CharField(max_length=20, verbose_name='direccion')
    region = models.CharField(max_length=20, verbose_name='Región')
    email = models.EmailField(verbose_name='Email')
    email2 = models.EmailField(verbose_name='Reingrese su Email')
    pais = models.CharField(max_length=20, verbose_name='Pais')
    contrasenna = models.CharField(max_length=12, verbose_name='Contraseña')
    contrasenna2 = models.CharField(max_length=12, verbose_name='Reingrese su Contraseña')
    moneda_pago = models.CharField(max_length=10, verbose_name='Moneda de pago: pesos/dólares')


    def __str__(self):
        return self.numId
