from django.db import models

class User(models.Model):
    EIN = models.IntegerField(max_length=9)
    email = models.EmailField()
    business_name = models.CharField(max_length=200)
    
