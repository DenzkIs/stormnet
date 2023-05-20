from django.http import HttpResponse
from django.shortcuts import render

from .forms import AllForm


def get_page_forms(request):
    form = AllForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AllForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    return render(request, 'forms2_page.html', context)
