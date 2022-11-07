from django.core.checks import messages
from django.db.models.fields import URLField
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView, View, FormView, edit
from django.http import HttpResponse, request
from employee.forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.

class Home(TemplateView):
       template_name='index.html'

class EmployeeListView(ListView):
    template_name = "emplists.html"
    model = Employee
    context_object_name='employees'


    def post(self,request,*args,**kwargs):
       
        employees = Employee.objects.all()
        
        if request.POST['name']:
            employees = employees.filter(user__first_name__icontains=request.POST['name'])
        if request.POST['department']:
            employees = employees.filter(department=request.POST['department'])
        if request.POST['designation']:
            employees = employees.filter(designation=request.POST['designation'])
            
        context = self.get_context_data()
        context['employees'] = employees
        return self.render_to_response(context=context)   
    
     
           
class EmployeeDetailView(DetailView):
    template_name = "detail.html" 
    model =Employee
    context_object_name = 'Employee'
    
class EmployeeView(FormView):
    template_name = 'signup.html'   
    form_class = EmployeeForm
    
      
    def form_valid(self,  form):
       
        
        name = form.data['name']
        username = form.data['username']
        password = form.data['password']
        user = User.objects.create_user(username=username,password=password,first_name=name)
        
        Employee.objects.create(user=user,**form.cleaned_data)
        
        
        return self.render_to_response( context= {'message': "Thank you "})

class LoginView(View):
    template_name = 'login.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
    def POST(self,request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(request,username=username,password=password)
            if user is not None :
                login(request,user)
                employee = Employee.objects.filter(user=user).first()
                if employee:
                    return redirect(reverse_lazy( 'home'))
                            
            else:
                return render(request, self.template_name, context={'error_message': "Specify user"} )
        return render(request, self.template_name,context={'error_message': "Specify username and password"} )
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy( 'login'))


class AttendanceView(FormView):
    
	template_name = 'attendance.html'
	form_class   = AttendanceForm

	def get(self,request):
		context = self.get_context_data()
  			
		employee = Employee.objects.filter(user= request.user).first()
		if employee:
			return render(request,self.template_name,context)
		else:
			context['error_message']="Employee has not logged in"
			return render(request,self.template_name, context=context)
                
	def form_valid(self,form):
		if self.request.user:
			user = self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name, context= {'error_message' : "Employee has not logged in "})
			employee = Employee.objects.filter(user=user).first()
			if employee:
				Attendance.objects.create(attendance_for = employee,**form.cleaned_data)
				return self.render_to_response( context= {'message': "Thank you for Attendance "})
         
class MaterialView(FormView):
    
	template_name = 'material.html'
	form_class = MaterialForm
 x
	def get(self,request):
		context = self.get_context_data()
		employee  = Employee.objects.filter(user=request.user).first()
		if employee:
					return render(request,self.template_name,context)
		else:
			context['error_message'] = "Employee has not logged in "
			return render(request,self.template_name, context= context)

	def form_valid(self,form):
		if self.request.user:
			user =  self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name, context= {'error_message': "Employee has not logged in"})

			employee = Employee.objects.filter(user = user).first()
			if employee:
				Material.objects.create(requestor = employee, **form.cleaned_data)
				return self.render_to_response(context={'message':"Thank you for info"})
      
class TransportView(FormView):
	template_name = 'transport.html'
	form_class = TransportForm

	def get(self,request):
		context = self.get_context_data()
		if request.user:
			user = request.user
			if(user.is_anonymous):
				context['error_message'] = "User has not logged in "
				return self.render_to_response( context= context)  
			else:
				employee = Employee.objects.filter(user=user).first()
				if employee:
					return render(request, self.template_name, context)
				else:
					context['error_message'] = "Employee has not logged in "
					return render(request,self.template_name,  context= context)  
    
	def form_valid(self,form):	
		if self.request.user:
			user = self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name,  context= {'error_message' : "Employee has not logged in "})  

			employee = Employee.objects.filter(user=user).first()
			if employee:
				Transport.objects.create(requestor=employee, **form.cleaned_data)        
				return self.render_to_response( context= {'message': "Thank you for info "})  

class ApprasialView(TemplateView):
	template_name = 'apprasial.html'
	form_class = ApprasialStepForm
	
	def get_context_data(self, **kwargs):
		context =  super().get_context_data(**kwargs)
		user = self.request.user
		if (user.is_anonymous):
			context['error_message'] = 'User is Not logged in'
		else:
			employee = Employee.objects.filter(user=user).first()
			appraisal = Apprasial.objects.filter(appraisee=employee).first()
			steps = appraisal.steps.all()
			context['steps'] = steps
		return context	
	
	
class ApprasialResultView(View):
	template_name = 'result.html'
	form_class = ApprasialResultForm
	
 
	def form_valid(self,form):
		if self.request.user:
			user = self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name, context= {'error_message' : "Employee has not logged in "})
			employee = Employee.objects.filter(user=user).first()
			if employee:
				ApprasialStep.objects.create(apprasial = employee,**form.cleaned_data)
			return self.render_to_response( context= {'message': "Thank you  "})
	

class LeaveView(FormView):
	template_name = 'leave.html'
	form_class = LeaveForm
	
	def get(self,request):
		context = self.get_context_data()
  			
		employee = Employee.objects.filter(user = request.user).first()
		if employee:
			context['approval_leaves'] = Leave.objects.filter(approver=employee)
			return render(request,self.template_name,context)
		else:
			context['error_message']="Employee has not logged in"
			return render(request,self.template_name, context=context)
                
	def form_valid(self,form):
		if self.request.user:
			user = self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name, context= {'error_message' : "Employee has not logged in "})
			employee = Employee.objects.filter(user=user).first()
			if employee:
				Leave.objects.create(requestor=employee,**form.cleaned_data)
				return self.render_to_response( context= {'message': "Enjoy the Leave "})


class OverTime(FormView):
	template_name = 'overtime.html'
	form_class = OverTimeForm
 
	def get(self,request):
		context = self.get_context_data()
  			
		employee = Employee.objects.filter(user = request.user).first()
		if employee:
			context['approval_overtime'] = OverTime.objects.filter(approver = employee)
			return render(request,self.template_name,context)
		else:
			context['error_message']="Employee has not logged in"
			return render(request,self.template_name, context=context)
                
	def form_valid(self,form):
		if self.request.user:
			user = self.request.user
			if(user.is_anonymous):
				return render(request,self.template_name, context= {'error_message' : "Employee has not logged in "})
			employee = Employee.objects.filter(user=user).first()
			if employee:
				OverTime.objects.create(requestor=employee,**form.cleaned_data)
				return self.render_to_response( context= {'message': "Enjoy the Leave "})
