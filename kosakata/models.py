from django.db import models

# Create your models here.

class Kosakata(models.Model):
    kata = models.CharField(max_length=100)
