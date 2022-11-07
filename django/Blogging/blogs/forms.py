from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import *  
from .models import *
from django.forms.fields import DateField
from .views import *

        
#use widgets to put placeholder & to create password type filed       
class RegisteringForm(ModelForm):
    
    
    
	def __init__(self, *args, **kwargs):
		super(RegisteringForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'last Name'
		self.fields['username'].widget.attrs['placeholder'] = 'username'
		self.fields['password'].widget.attrs['placeholder'] = 'password'
		
	class Meta:
		model = User
		exclude = ('date_joined',)
        
	


class SearchForm(ModelForm):
    class Meta:
          
        fields = '__all__'  

