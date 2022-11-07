from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    
    path('blog_detail/<str:slug>/',BlogDetailView.as_view(),name='detail'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('blog_catergorie/<str:slug>',CategorieView.as_view(),name = 'catergory'),
    path('search/',SearchView.as_view(),name='search'),
    path('signup/',SignUpView.as_view(),name='signup')  ,   
]
