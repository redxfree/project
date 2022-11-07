from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.
class Catergory(models.Model):
	category = models.CharField(max_length=300)
	
	

class Products(models.Model):
	name = models.CharField(max_length=100)
	pic  = models.ImageField()
	price = models.IntegerField()
	category = models.ForeignKey(Catergory,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
	
	
class cart(models.Model):
	cart_user = models.OneToOneField(User,on_delete=models.CASCADE)
	added = models.DateTimeField(auto_now_add=True)
	items = models.ForeignKey(Products,on_delete=models.CASCADE)
	
	
