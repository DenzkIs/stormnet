from django import forms
from django.core.exceptions import ValidationError

from .models import Info


class InfoForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = ("name", "surname", "age")
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "И"}),
            'surname': forms.TextInput(attrs={"placeholder": "Фамилия"}),
            'age': forms.TextInput(attrs={"placeholder": "Возраст"}),
        }

    def clean_age(self):
        print(self.cleaned_data)
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError("Еще слишком мал")
        return age

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise ValidationError("Только текст")
        return name
