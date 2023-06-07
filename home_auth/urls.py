from django.urls import path
from .views import get_login, get_logout, get_registration, get_uniq_reg


urlpatterns = [
    path('', get_login, name='login'),
    path('logout/', get_logout, name='logout'),
    path('registration/', get_registration, name='registration'),
    path('uniq_reg/', get_uniq_reg, name='uniq_reg'),

]