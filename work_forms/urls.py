from django.urls import path

from .views import *

urlpatterns = [
    path('', get_page_all_forms, name='forms_page'),
    path('people/', get_people_form, name='people_form'),

]
