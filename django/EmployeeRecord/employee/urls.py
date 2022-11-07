from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('',Home.as_view(),name='home' ),
    path('list/',EmployeeListView.as_view(),name='list'),
    path('detail/<int:pk>/',EmployeeDetailView.as_view(),name='detail'),
    path('signup/',EmployeeView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('attendance/',login_required(AttendanceView.as_view(),login_url='/employee/login/'),name='attendance'),
    path('material/',login_required(MaterialView.as_view(),login_url='/employee/login/'),name='material'),
    path('transport/',login_required(TransportView.as_view(),login_url='/employee/login/'),name='transport'),
    path('apprasial/',login_required(ApprasialView.as_view(),login_url='/employee/login'),name='apprasial'),
    path('result/',login_required(ApprasialResultView.as_view(),login_url='/employee/login'),name='result'),
    path('leave/',login_required(LeaveView.as_view(),login_url='/employee/login'),name='leave'),
    path('overtime/',login_required(OverTime.as_view(),login_url='/employee/login'),name='overtime')
            
]
