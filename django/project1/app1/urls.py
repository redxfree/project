from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home_view, name='home'),
    path('etc/', etc_view, name='etc'),
    path('hello/', hello_view, name='hello'),
    path('start/', start_view, name='start'),
    path('start1/', start1_view, name='start1'),
    
   
     path('home2/',HomeView.as_view() , name='home2'),
     path('home_list/',HomeListView.as_view() , name='home_list'),
     path('home_detail/<int:pk>/',HomeDetailView.as_view() , name='home_detail'),
     path('employee_list/',EmployeeListView.as_view() , name='employee_list'),
     path('employee_detail/<int:pk>/',EmployeeDetailview.as_view() , name='employee_detail')
     
]