from django.urls import path

from .views import get_model_form

urlpatterns = [
    path('', get_model_form, name='model_form')
]
