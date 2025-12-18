from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField()


