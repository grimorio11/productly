from django.contrib import admin
from .models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'puntaje', 'categoria', 'creado_en')
    search_fields = ('nombre', )
    list_filter = ('categoria', )
    ordering = ('-creado_en', )
    
# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)