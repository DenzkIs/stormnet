from django.db import models


class Cars(models.Model):

    color = models.CharField(max_length=100)
    picture = models.ImageField(blank=True)
