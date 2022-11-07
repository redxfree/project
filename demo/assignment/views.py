from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
# Create your views here.

class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemEdit(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

class SerachItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['$name']