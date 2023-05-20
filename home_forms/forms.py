from django import forms
from .models import *

class AllForm(forms.Form):
    CHOICE = (
        ('0', ''),
        ('1', 'Johan'),
        ('2', "Johan's brother"),
        ('3', "Johan's sister"),
    )

    bool_field = forms.BooleanField(initial=True)
    char_field = forms.CharField(label='Просто текст', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'до 255 символов'}))
    date_field = forms.DateField(help_text='YYYY-MM-DD')
    datetime_field = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'ГГГГ-ММ-ДД ЧЧ:ММ'}))
    decimal_field = forms.DecimalField(decimal_places=2, max_digits=5)
    email_field = forms.EmailField()
    file_field = forms.FileField(required=False)
    image_field = forms.ImageField(required=False)
    mult_filed = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=CHOICE)
    example = forms.ModelChoiceField(queryset=ExampleModel.objects.all(), label='Пример')

