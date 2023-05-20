from django.urls import path

from .views import get_products, get_all_products_category, add_product

urlpatterns = [
    path('', get_products, name='all'),
    path('category/<int:id>', get_all_products_category, name='category'),
    path('add_product/', add_product, name='add_product'),

]
