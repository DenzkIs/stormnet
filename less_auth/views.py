from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_my(request):
    context = {}
    form = UserCreationForm()
    context['form'] = form
    if request.method == "POST" and 'login' in request.POST:
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        # user = User.objects.get(username=request.POST.get('username'))
        if user is not None:
            login(request, user)
        else:
            context['cannot_find_user'] = \
                'Ты что-то не правильно ввел, попробуй еще раз или зарегистрируйся по форме ниже'

    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
    
    if request.method == 'POST' and 'registration' in request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
    return render(request, 'login_my.html', context)
