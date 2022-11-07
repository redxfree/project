from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import TemplateView, DetailView, ListView, View, FormView
from app.forms import PersonForm
from .models import *


    
class PersonListView(ListView):
    model = Person
    template_name = "list.html"
    ordering = ['name']
    
   
    
class PersonDetailView(DetailView):
    Model = Person
    template_name = "detail.html"
    
    
    def get_queryset(self):
        return Person.objects.filter()
    
    
def name_view(request):
    context= ('')
    context['persons'] = Person.objects.filter(gender ='male')
    return render (request, 'name.html', context)

class HomeView(TemplateView):
    template_name = "name.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.filter(age__gt=45)
        return context

class PostView(View):
    template_name = 'takename.html'
    pform = PersonForm()
    def get(self, request):
        return render(request, self.template_name, context={'message': "Fill your details", 
                                                            "form": self.pform})
    
    def post(self, request):
        name = request.POST.get('name')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        
        Person.objects.create(name=name, age=int(age), city=city, gender=gender)
        
        
        return render(request, self.template_name, context={'message': "Thank you "})
    

class PersonPostView(FormView):
    template_name = 'takename2.html'
    form_class = PersonForm
    
  
    def form_valid(self,  form):
       
        print("I am in view PersonPostView")
        Person.objects.create(**form.cleaned_data)
        
        
        return self.render_to_response( context= {'message': "Thank you "})
                    

