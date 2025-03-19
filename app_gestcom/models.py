from django.db import models

# Create your models here.
class Categorie(models.Model):
    code = models.CharField(max_length=10,primary_key=True)
    designation = models.CharField(max_length=100,unique=True)
