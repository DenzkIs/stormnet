from django.urls import path

from .views import get_page_forms

urlpatterns = [
    path('', get_page_forms, name='forms2_page')
]
