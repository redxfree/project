from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import DateInput, SelectDateWidget, TimeInput, NumberInput  
from .models import *
from django.forms.fields import DateField,TimeField 
from .views import *

class EmployeeForm(ModelForm):
    dob = forms.DateField(widget=DateInput(attrs={'type':'date'})) 
                                         
    class Meta:
        model = Employee
        exclude = ['user',]
        

        
class AttendanceForm(ModelForm):
    attendance_date = forms.DateField(widget=DateInput(attrs={'type':'date'})) 
    in_time = forms.DateField(widget=DateInput(attrs={'type':'time'}))
    out_time = forms.DateField(widget=DateInput(attrs={'type':'time'}))
     
    class Meta:
        model = Attendance
        exclude = ['attendance_for']
              
class MaterialForm(ModelForm):
       
    class Meta:
        model = Material
        exclude =  ['requestor']   
        
        
class TransportForm(ModelForm):
       
    class Meta:
        model = Transport
        exclude = ['requestor']
                
 
class ApprasialStepForm(ModelForm):
    
    class Meta:
        model = ApprasialStep
        fields = '__all__'
        
class ApprasialResultForm(ModelForm):
    class Meta:
        model = ApprasialResult
        fields = '__all__'
        
        

        
class OverTimeForm(ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type':'date'})) 
    timefrom = forms.DateField(widget=DateInput(attrs={'type':'time'}))
    timeto = forms.DateField(widget=DateInput(attrs={'type':'time'}))

    class Meta:
        model = OverTime
        exclude = ['employee','status']
        

class LeaveForm(ModelForm):
    leavedate = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    enddate = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    class Meta:
        model = Leave
        exclude = ['requestor','status']