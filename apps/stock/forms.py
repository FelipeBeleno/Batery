from django.forms import *
from apps.stock.models import *
from widget_tweaks import *


class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoria',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripcion de la categoria'
                }
            )

        }


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'categoria': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese El nombre del articulo'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion del producto',
                    'rows': '3'
                }
            ),
            'precio': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'imagen': FileInput(
                attrs={
                    'class': 'custom-file form-control'
                }
            ),
            'stock': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }
