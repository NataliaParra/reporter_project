from django.contrib import admin

# Register your models here.
#solo el punto porque es la carpeta en la que se encuentra
from .models import Galleta, Proveedor, Sabor

admin.site.register([Galleta, Proveedor, Sabor])