from .models import cart,Products,Catergory
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout 
from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework.backends import DjangoFilterBackend
# Create your views here.


class RegisterAPI(generics.GenericAPIView):
	serializer_class = Registerserializers
	template_name = 'app/register.html'
		
	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		
		return Response({
			"Mesaage" : "Registered successfully"
		})
  	
			
class LoginApi(generics.GenericAPIView):
	serializer_class = LoginSerializer
	template_name = 'app/login.html'
		
	def post(self, request, format=None):
		serializer = AuthTokenSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		
		
		return redirect(reverse_lazy('home'))
	   		
class LogoutApi(generics.GenericAPIView):
	 
	def get(self,request):
		logout(request)
		return redirect(reverse_lazy('login'))
	
	
class Product(generics.ListAPIView):
	queryset = Products.objects.all()
	serializer_class = Productserializers
	template_name = 'app/home.html'
	renderer_classes = [TemplateHTMLRenderer]

	def get(self,request):
		item =Products.objects.all()
		context = {
			'item' : item
		}
		return render(request,self.template_name,context)
	
class Productdetail(generics.RetrieveAPIView):
	queryset = Products.objects.all()
	serializer_class = Productserializers
	template_name = 'app/product.html'
	
		
	def get_serializer_class(self):
    
		if hasattr(self, 'action_serializers'):
			return self.serializer_class.get(self.action, self.serializer_class)

		return super(Productdetail,self).get_serializer_class()


class categorie(generics.ListAPIView):
	queryset = Catergory.objects.all()
	serializer_class = categoryserailizers
	filter_backends = [DjangoFilterBackend]
	search_fields = ['Dress','Laptop','MObile']

	
 
class cartList(generics.ListAPIView):
	queryset = cart.objects.all()
	serializer_class = cartserializers

	
	
class cartdetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = cart.objects.all()
	serializer_class = cartserializers
	