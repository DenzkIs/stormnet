from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def get_login(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
    return render(request, 'home_auth.html')


def get_logout(request):
    logout(request)
    return redirect('login')


def get_registration(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')

        if validate_password(password1, password2):
            clean_password = password1
        else:
            context['not_equal'] = 'Passwords not equal'
            clean_password = ''

        if length_check(first_name):
            clean_first_name = first_name
        else:
            context.update({'too_long': 'Too long'})
            clean_first_name = ''

        if clean_password and clean_first_name:
            user = User(username=username, password=clean_password, email=email, first_name=clean_first_name)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            context.update({'clean_username': username, 'clean_email': email, 'clean_first_name': clean_first_name})
            return render(request, 'registration.html', context)

    return render(request, 'registration.html', context)


def validate_password(password_1, password_2):
    if password_1 == password_2:
        return True


def length_check(text):
    if len(text) < 4:
        return True
