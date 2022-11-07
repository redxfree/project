from django.db import models
from django.db.models import Q

class Student(models.Model):
    name = models.CharField(max_length=127)
    age = models.IntegerField()
    course = models.CharField(max_length=127)
    
    def __str__(self):
        return self.name

#Create Employee Model(name, department, age, salary(auto:id/pk)
# Create a List view.
# Create template for list view(students.html)
# Display employee data in a table
# Make student name as hyperlink- to detail view
# Create Detail View
# Create template for detail view.(studentdetail.html)
# Display Employee data in seperate lines and make name bold

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name

