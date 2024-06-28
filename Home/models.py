from django.db import models

# Create your models here.

class vc(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)