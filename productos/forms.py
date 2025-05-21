from . import models
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria', 'creado_en']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'stock': NumberInput(attrs={'class': 'form-control'}),
            'puntaje': NumberInput(attrs={'class': 'form-control'}),
            'categoria': Select(attrs={'class': 'form-control'}),
            'creado_en': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }