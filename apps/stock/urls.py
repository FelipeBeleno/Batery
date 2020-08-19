from django.urls import path

from apps.stock.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, \
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

app_name = 'stock'

urlpatterns = [

    # Urls Para Categorias
    path('list/', CategoriaListView.as_view(), name='ListaCategorias'),
    path('create/', CategoriaCreateView.as_view(), name='CrearCategorias'),
    path('update/<pk>/', CategoriaUpdateView.as_view(), name='EditarCategorias'),
    path('delete/<pk>/', CategoriaDeleteView.as_view(), name='EliminarCategorias'),

    # Urls Para Productos
    path('listProductos/', ProductoListView.as_view(), name='ListaProductos'),
    path('createProductos/', ProductoCreateView.as_view(), name='CrearProductos'),
    path('updateProducto/<pk>/', ProductoUpdateView.as_view(), name='EditarProductos'),
    path('deleteProducto/<pk>/', ProductoDeleteView.as_view(), name='EliminarProductos'),

]
