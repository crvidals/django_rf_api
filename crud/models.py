from django.db import models

class Empresas(models.Model):
    name_company = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    sector = models.CharField(max_length=200)
    fundator = models.CharField(max_length=200)
    description = models.TextField()
    rut = models.CharField(max_length=300)
    email = models.EmailField(max_length = 300)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Personas(models.Model):
    full_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    age = models.IntegerField()
    description = models.TextField()
    rut = models.CharField(max_length=300)
    email = models.EmailField(max_length = 300)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)