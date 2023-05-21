from django import forms
from django.core.exceptions import ValidationError

from .models import Info


class InfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields.get('name').__dict__)

    class Meta:
        model = Info
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Имя"}),
            'surname': forms.TextInput(attrs={"placeholder": "Фамилия"}),
            'age': forms.TextInput(attrs={"placeholder": "Возраст"}),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError("Еще слишком мал")
        return age
