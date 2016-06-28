from django.db import models

# Create your models here
class Marksheet(models.Model):
    f = models.FileField(upload_to='files/')
    n = models.PositiveIntegerField()
    t = models.PositiveIntegerField()
    c = models.CharField(max_length = 4)

class Image(models.Model):
    i = models.ImageField(upload_to='images/')
