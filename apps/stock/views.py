from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.stock.forms import CategoriaForm, ProductoForm
from apps.stock.models import Categorias, Producto


class CategoriaListView(ListView):
    template_name = 'Categoria/List.html'
    context_object_name = 'catagoria'
    model = Categorias


class CategoriaCreateView(CreateView):
    template_name = 'Categoria/Create.html'
    context_object_name = 'categoria'
    form_class = CategoriaForm
    model = Categorias
    success_url = reverse_lazy('stock:ListaCategorias')


class CategoriaUpdateView(UpdateView):
    template_name = 'Categoria/Create.html'
    context_object_name = 'categoria'
    form_class = CategoriaForm
    model = Categorias
    success_url = reverse_lazy('stock:ListaCategorias')


class CategoriaDeleteView(DeleteView):
    template_name = 'Categoria/Delete.html'
    context_object_name = 'categoria'
    model = Categorias
    success_url = reverse_lazy('stock:ListaCategorias')


class ProductoListView(ListView):
    template_name = 'Productos/List.html'
    context_object_name = 'producto'

    def get_queryset(self):
        lista = Producto.objects.all()
        return lista


class ProductoCreateView(CreateView):
    template_name = 'Productos/Create.html'
    form_class = ProductoForm
    model = Producto
    success_url = reverse_lazy('stock:ListaProductos')


class ProductoUpdateView(UpdateView):
    template_name = 'Productos/Create.html'
    form_class = ProductoForm
    model = Producto
    success_url = reverse_lazy('stock:ListaProductos')


class ProductoDeleteView(DeleteView):
    template_name = 'Productos/Delete.html'
    model = Producto
    success_url = reverse_lazy('stock:ListaProductos')
