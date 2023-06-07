from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100, verbose_name="First name")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id}-{self.name}'


class Session2(models.Model):
    session2_id = models.CharField(max_length=100)
    count = models.IntegerField()
    time_create = models.TimeField(auto_now=True)

    def __str__(self):
        return self.session2_id
