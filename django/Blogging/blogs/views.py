from django.core.paginator import *
from django.template import context
from .forms import RegisteringForm
from .models import *
from django.views.generic import  *
from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.http import *
from django.urls import reverse_lazy

from django.db.models import *



class HomeListView(ListView):
	template_name = 'index.html'
	model = Blog
	paginate_by = 3
	context_object_name = 'blogs'	
 
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		
		context['Catergorie'] = Catergorie.objects.all()
		return context
        
class BlogDetailView(DetailView):
	model = Blog
	template_name = "detail.html"
	context_object_name = 'blog'
	
	def post(self,request):
		comment = request.POST['comment']
		blog = request.POST['blog']
		user = request.user
   
		comment = Comment.objects.create(comment=comment,blog=blog,blog_user=user)

	
		return self.render_to_response(context = {'message': "Successfully Commented "})

class SignUpView(FormView):
	template_name = 'signup.html'   
	form_class = RegisteringForm
	
	def form_valid(self,form):
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
        
		#print('first_name = '+ first_name)

		User.objects.create_user(first_name=first_name,last_name=last_name, username=username,password=password )
		return self.render_to_response(context = {'message': "Successfully Created "})
		

class LoginView(TemplateView):
	template_name = 'login.html'

 
	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect(reverse_lazy('home'))
		context = self.get_context_data()
		context['error_message'] = "user not found"
		return self.render_to_response(context=context )		
   
   
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse_lazy('login'))
    
    

	
class SearchView(View):
	template_name = 'search.html'
			
	def post(self,request):
		q = request.POST.get()
		blogs = Blog.objects.filter(Q(title_icontains = q),Q(title_icontent = q),Q(title_catergorie = q))
		context = self.get_context_data()
		context['blogs'] = blogs
		
		return redirect(reverse_lazy('home'))
	
 
class CategorieView(View):
    template_name = 'category.html'
    
    def post(self,request):
        
        cat = Catergorie.objects.filter(context = cat) 		
        return render(request,context)