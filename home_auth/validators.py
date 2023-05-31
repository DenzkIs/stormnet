import re
from email_validator import validate_email, EmailNotValidError
error = ''

def validate_password(password_1, password_2):
    if password_1 == password_2:
        return True


def validate_firstname(text: str):
    if len(text) < 16 and ' ' not in text and text.isalpha():
        return True


def validate_unique_username(text, model_user):
    """
    Использовать только с моделью User
    """
    names = []
    for md in model_user.objects.all():
        names.append(md.username.lower())

    if text.lower() not in names:
        return True
    # if not bool(model_name.objects.filter(username=text.lower())):
    #     return True


def validate_unique_email(email, model_user):
    """
    Использовать только с моделью User
    """
    emails = []
    for md in model_user.objects.all():
        emails.append(md.email.lower())

    if email.lower() not in emails:
        return True


def my_validate_email(email, regex):
    if regex == 'no':
        characters = 'abcdefghijklmnopqrstuvwxyz.@_-'
        email = email.lower()
        if email.count('@') != 1 or len(email) > 50:
            return False
        name, domen = email.split('@')
        print(name, '---', domen)
        if domen.count('.') != 1:
            return False
        for i in name:
            if i not in characters:
                return False
        dom, country = domen.split('.')
        print(dom, '----', country)
        if not dom.isalpha() or not country.isalpha() or len(dom) < 2 or len(country) < 2:
            return False
        return True
    elif regex == 'yes':
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, email) is not None:
            print('I am here')
            return True
    else:
        try:
            # print(email)
            email_info = validate_email(email, check_deliverability=True)
            # print(email_info)
            good_email = email_info.normalized
            print(good_email)
            return True
        except EmailNotValidError as e:
            # Как отобразить Error в шаблоне?
            error = str(e)
            print(error)
