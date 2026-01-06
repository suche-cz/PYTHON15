from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField()


class Baby(models.Model):
    mother = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    weight = models.FloatField(blank=True, null=True, help_text='Zadejte váhu v kg při narození')
    height = models.FloatField(blank=True, null=True, help_text='Zadejte výšku v cm při narození')

    def __str__(self):
        return self.name


class Growth(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(help_text='Zadejte váhu v kg při')
    height = models.FloatField(help_text='Zadejte výšku v cm při')
    note = models.TextField(max_length=200, blank=True)




"""

Tasky:



"""


"""
1. virtuální prostředí
- instalace virtuálního prostředí
- aktivace virtuálního prostředí

2. vytvoření projektu

3. spuštění projektu
- python manage.py runserver
"""
