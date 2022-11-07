from django.views.generic import detail
from .views import *
from django.urls import path

urlpatterns = [
    path('list',PersonListView.as_view(),name ='list'),
    path('detail/<int:pk>/',PersonDetailView.as_view(),name='detail'),
    path('name',name_view,name = 'name = name'),
    path('home',HomeView.as_view(),name= 'home'),
    path('addperson/',PostView.as_view(),name= 'addperson'),
    path('addperson2/',PersonPostView.as_view(),name= 'addperson2')
    
    
]