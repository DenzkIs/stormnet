from django import forms
from django.core.exceptions import ValidationError

from .models import People


def get_bmw(value):
    if value != 'BMW':
        raise ValidationError('Не BMW')


class CarForm(forms.Form):
    brand = forms.CharField(validators=[get_bmw, ])
    model = forms.CharField()
    number = forms.IntegerField(max_value=10, min_value=0)
    price = forms.DecimalField()
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'ГГГГ-ММ-ДД', 'class': 'johan'}))

    def clean_brand(self):
        return self.cleaned_data.get('brand') + ' немецкая тачка'


class PeopleForm(forms.ModelForm):
    group = forms.CharField()

    class Meta:
        model = People
        fields = '__all__'
