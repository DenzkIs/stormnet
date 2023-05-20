from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .models import *


def get_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {"categories": categories, "products": products}
    if request.method == 'POST':
        input_login = request.POST.get('login')
        if not bool(Person.objects.filter(login=input_login)):  # получаем булевое значение пустого (или нет) QuertSet
            person = Person(login=input_login, password=request.POST.get('password'))
            person.save()
            messages.success(request, 'Сохранил в БД')
            pers = Person.objects.last()
            context["pers"] = pers
        else:
            messages.warning(request, 'Логин занят, попробуй сохранить другой!!!')
    return render(request, 'page_products.html', context)


def get_all_products_category(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories_id=id)
    context = {"categories": categories, "products": products}

    return render(request, 'page_products.html', context)


def add_product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"categories": categories, "products": products}
    if request.method == 'POST' and request.FILES:
        print(request.POST)
        print(request.FILES)
        new_prod = Product(title=request.POST.get('title'), description=request.POST.get('description'),
                           price=request.POST.get('price'), image=request.FILES.get('image'),
                           categories_id=int(request.POST.get('categories')))
        new_prod.save()
        messages.success(request, 'Продукт добавлен')

    return render(request, 'add_product.html', context)
