from django.db import models

class Members(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
# Create your models here.
