from django.db import models
from datetime import datetime 

# Create your models here.
class Writer(models.Model):
    name = models.fields.CharField(max_length=100)
    born = models.fields.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    name = models.fields.CharField(max_length=100, primary_key=True, null=False, blank= False)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, null=True, blank=True)
    year = models.fields.IntegerField(null=True, blank=True)
    rec1 = models.fields.CharField(max_length=120,null=True,blank=True)
    rec2 = models.fields.CharField(max_length=120,null=True,blank=True)
    rec3 = models.fields.CharField(max_length=120,null=True,blank=True)
    last_update = models.fields.DateTimeField(auto_now_add=True, blank=True)
