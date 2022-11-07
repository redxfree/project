
from django.urls import path
from .views import *

urlpatterns = [
    path('create/',ItemCreateAPIView.as_view(),name='create'),
    path('list/',ListItem.as_view(),name='list'),
    path('edit/<int:pk>',ItemEdit.as_view(),name='edit'),
    path('search/',SerachItem.as_view(),name='search')
]
