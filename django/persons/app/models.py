from django.db import models
from django.db.models import Q

# Create your models here.
class Person(models.Model):
    GENDERS = (("M", "Male"), ("F", "Female"))
    
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    city = models.CharField(max_length=50)
    
    
    def __str__(self):
        return '%s - %s' %(self.name , str(self.age),)
    