from django.db import models, IntegrityError

errors = {}


class UniqSave(models.Model):
    name = models.CharField(max_length=255, unique=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            errors.update({'unique': f'Пользователь с именем {self.name} уже существует'})
