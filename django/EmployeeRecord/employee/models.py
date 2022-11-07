from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from django.db.models.fields import DateField, TimeField
from django.db.models.lookups import IContains
from django.db.models.manager import Manager
from django.forms import widgets

# Create your models here.
class Designation(models.Model):
    designation = models.CharField(max_length=127)
    
    def __str__(self):
        return self.designation
    
class Department(models.Model):
    department = models.CharField(max_length=127)
    
    def __str__(self):
        return self.department
    
class Employee(models.Model):
    
	GENDERS = (('M','Male'),('F','Female'))
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField()
	department = models.ForeignKey(Department,on_delete=models.CASCADE)
	designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
	salary = models.DecimalField(max_digits=10,decimal_places=2)
	gender = models.CharField(max_length=1,choices= GENDERS)
	contact = models.CharField(max_length=10)
	joining_date = models.DateField(null=True,blank=True)
	exit_date = models.DateField(null=True,blank=True)
	dob =models.DateField(null=True,blank=True)
	employee_imaage = models.ImageField(upload_to="images/employees",  blank=True)
    
	def __str__(self):
		return self.user.first_name  

	property
	def salary_per_hour(self):
		self.salary/(30*8)
	
class OverTime(models.Model):
	STATUS = (('P','Pending'),('A','Approved'),('R','Rejected'))
	date = models.DateField()
	timefrom = models.TimeField()
	timeto = models.TimeField()
	employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
	approver = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='approver')
	status = models.CharField(max_length=1,choices=STATUS)
    
	def __str__(self):
		return '%s-%s-%s-%s-%s'  %(str(self.date), str(self.timefrom),str(self.timeto),str(self.employee),str(self.approver))


class Attendance(models.Model):
    attendance_for = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='attendance')
    attendance_date = models.DateField()
    in_time = models.TimeField() 
    out_time = models.TimeField() 
    
    def __str__(self):
        return '%s-%s'  %(str(self.attendance_for), self.attendance_date)
    
class Apprasial(models.Model):
	appraisee = models.ForeignKey(Employee,on_delete=CASCADE, related_name='appraisals')
	a_date = models.DateTimeField(auto_now_add=True)
	appraiser = models.ForeignKey(Employee,on_delete=CASCADE, related_name='appraisals_taken')
    
	def __str__(self):
		return '%s appraisal taken by %s'  %(str(self.appraisee), self.appraiser)


class ApprasialStep(models.Model):
	appraisal = models.ForeignKey(Apprasial,on_delete=CASCADE, related_name='steps')
	question = models.CharField(max_length=1023)
	answer = models.CharField(max_length=1023, blank=True)
	def __str__(self):
		return '%s - %s'  %(str(self.appraisal), self.question)

class ApprasialResult(models.Model):
	RESULTS = (('P','Promoted'),('S','Salary Hike'), ('N','No Hike'))
	appraisal = models.ForeignKey(Apprasial,on_delete=CASCADE)
	result = models.CharField(max_length=1, choices=RESULTS)
	
	def __str__(self):
		return '%s - %s'  %(str(self.appraisal), self.result)

class AvailableMaterial(models.Model):
	
	material = models.CharField(max_length=250)
	
	def __str__(self):
		return self.material

class Material(models.Model):
	requestor = models.ForeignKey(Employee,on_delete=CASCADE, related_name='askedby')
	material = models.ForeignKey(AvailableMaterial, on_delete=models.CASCADE, related_name='askedfor')
	def __str__(self):
		return '%s-%s' %(str(self.requestor), str(self.material))


class Transport(models.Model):
	VEHICLES = (('B','Bus'),('C','Cab'))
	requestor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='transports')
	transport_from = models.CharField(max_length=150)
	transport_to = models.CharField(max_length=150) 
	vehicle   = models.CharField(max_length=1, choices= VEHICLES)
	cost_of_transport = models.DecimalField(max_digits=150,decimal_places=1)

	def __str__(self):
		return  '%s-%s' %(str(self.requestor), str(self.vehicle))

class Leave(models.Model):
	REASON =(('S','Sick'),('C','Casual'),('E','Emergency'),('M','Maternity'))
	STATUS = (('P','Pending'),('A','Approved'),('R','Rejected'))
	leavedate = models.DateField(null=True,blank=False)
	enddate = models.DateField(null=True,blank=False)
	leavetype = models.CharField(max_length=1,choices=REASON)
	status = models.CharField(max_length=1,choices=STATUS,default='pending')
	requestor = models.ForeignKey(Employee,on_delete=models.CASCADE)
	approver = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='approve') 
	def __str__(self):
		return '%s-%s-%s-%s-%s-%s' %(str(self.leavedate),str(self.enddate),str(self.leavetype),str(self.status),str(self.requestor),str(self.approver))

    
