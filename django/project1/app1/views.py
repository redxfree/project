from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django import forms
from .models import *

def home_view(request):
    context={'somedata': 'This is my data'}
    context['students'] = Student.objects.filter(age__gt=10)
    return context
    
    
class HomeView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.filter(age__gt=10)
        return context
    

class HomeListView(ListView):
    template_name = 'index.html'
    model = Student
    context_object_name = 'students'

class HomeDetailView(DetailView):
    template_name = 'student.html'
    model = Student
    context_object_name = 'students'
    
def etc_view(request):
    return HttpResponse('I am in etc')

def hello_view(request):
    return render(request,'booking.html')

def start_view(request):
    return render(request,'start.html')
    
def start1_view(request):
    return render(request,'start1.html')
    
class EmployeeListView(ListView):
    template_name = "employee.html"
    model = Employee
    context_object_name = 'employees'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Employee.objects.count()>0:
            total_age, total_salary =0
            for s in Employee.objects.all():
                total_age += s.age
                total_salary = s.salary
        
            context["average_age"] = total_age/Employee.objects.count()
            context["average_salary"] = total_salary/Employee.objects.count()
            
        return context
    
   
    
class EmployeeDetailview(DetailView):
    template_name = "employeedetail.html"
    model = Employee
    context_object_name = 'employee'               



