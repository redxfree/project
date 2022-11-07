from django.urls import path
from .views import LoginApi, LogoutApi, Product, Productdetail, RegisterAPI, cartList, cartdetail, categorie
from django.contrib.auth.decorators import login_required


urlpatterns = [
	path('home/',Product.as_view(),name='home'),
	
	
	path('login/',LoginApi.as_view(),name='login'),
	path('register/',RegisterAPI.as_view(),name='register'),
	path('logout/',LogoutApi.as_view(),name='logout'),
	path('product/<int:pk>/',Productdetail.as_view(),name='product'),
	path('cat/',categorie.as_view(),name='cat'),
#	path('cat/<int:pk>/',categoriedetail.as_view(),name='deatilcat'),
	path('cart/',cartList.as_view(),name='cart'),
	path('cartdetail/',cartdetail.as_view(),name='cartdetail') ,
	#path('pay/',Payment.as_view(),name='payl') ,
	   
	
]
