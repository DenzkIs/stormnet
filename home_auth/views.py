from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .validators import *
from .models import UniqSave, errors


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
        regex = request.POST.get('regex')

        if password1 == '':
            context['empty_password1'] = 'Cannot be empty'
            clean_password = ''
        else:
            if validate_password(password1, password2):
                clean_password = password1
            else:
                context['not_equal'] = 'Passwords are not equal'
                clean_password = ''
        if first_name == '':
            context['empty_firstname'] = 'Cannot be empty'
            clean_first_name = ''
        else:
            if validate_firstname(first_name):
                clean_first_name = first_name
            else:
                context.update({'too_long': 'Name must be shorter 15 symbols, without spaces, only letters'})
                clean_first_name = ''

        if username == '':
            context['empty_username'] = 'Cannot be empty'
            clean_username = ''
        else:
            if validate_unique_username(username, User):
                clean_username = username
            else:
                context.update({'not_unique_login': 'A user with that username already exists'})
                clean_username = ''

        if email == '':
            context['empty_email'] = 'Cannot be empty'
            clean_email = ''
        else:
            if my_validate_email(email, regex):
                email_norm = email
                if validate_unique_email(email_norm, User):
                    clean_email = email
                else:
                    clean_email = ''
                    context.update({'not_unique_email': 'The email already exist'})
            else:
                print('ERROR ---', error)
                if error:
                    context.update({'not_unique_email': error})
                    clean_email = ''
                else:
                    clean_email = ''
                    context.update({'not_unique_email': 'Incorrect email'})

        if clean_password and clean_first_name and clean_username and clean_email:
            user = User(username=clean_username, password=clean_password, email=clean_email,
                        first_name=clean_first_name)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            context.update({'clean_username': clean_username,
                            'clean_email': clean_email,
                            'clean_first_name': clean_first_name})
            return render(request, 'registration.html', context)

    return render(request, 'registration.html', context)


def get_uniq_reg(request):
    if request.method == 'POST':
        print(request.POST)
        test = UniqSave(name=request.POST.get('name'), count=request.POST.get('count'))
        test.save()
        return render(request, 'uniq_reg.html', errors)
    return render(request, 'uniq_reg.html')
