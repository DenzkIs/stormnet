from django.shortcuts import render

from .forms import CarForm, PeopleForm


# Create your views here.
def get_page_all_forms(request):
    form = CarForm()
    form1 = PeopleForm()
    context = {"form": form, 'form1': form1}
    if request.method == 'POST' and 'car_form' in request.POST:  # в dict прилетит ключ car_form = ''
        form = CarForm(request.POST)
        print(f'Заполненная форма до валидации - {form.data}')
        if form.is_valid():
            print(f'Cleaned_data внутри is_valid - {form.cleaned_data}')
        else:
            # form.is_bound = False  # отвязываем форму от данных, чтобы при ошибке отображать пустые поля
            print(f'Ошибки из else - {form.errors.as_data}')
            print(f'CLEANED_DATA без ошибок - {form.cleaned_data}')
            # form = CarForm(form.cleaned_data)
            context = {'form': form}
            # ^ отдаем в context форму, связанную с данными (в т.ч. ошибками)
    return render(request, 'forms_page.html', context)


def get_people_form(request):
    form = CarForm()
    form1 = PeopleForm()
    context = {"form": form, 'form1': form1}
    print(request.POST)
    if request.method == 'POST':
        form1 = PeopleForm(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data)
            form1.save()
    return render(request, 'forms_page.html', context)


