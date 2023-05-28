from django.urls import path

from .views import login_my

urlpatterns = [
    path('', login_my, name='login'),

]
