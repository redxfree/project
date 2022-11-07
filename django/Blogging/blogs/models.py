from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms import widgets
from django.db.models.fields import DateField
from django.utils.text import slugify
from django.db.models.lookups import IContains

class Catergorie(models.Model):
	catergorie = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150,unique=True)	
	def __str__(self):
		return self.catergorie

	
class Blog(models.Model):
	
	title = models.CharField(max_length=150)
	content = models.TextField()
	
	blog_image = models.ImageField(upload_to ="images/blogs", blank=True)
	created_date = models.DateField(auto_now_add=True)
	slug = models.SlugField(max_length=150,unique=True)
	categories = models.ManyToManyField(Catergorie)
	def __str__(self):
		return self.title
    
	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.title)
		super().save(*args, **kwargs)	
 

class Comment(models.Model):
    comment = models.TextField() #blog comment
    blog_user = models.ForeignKey(User,on_delete=models.CASCADE)
    coment_time = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
     
    def __str__(self):
        return self.comment   
    
