from dataclasses import fields
from itertools import product
from pyexpat import model
from rest_framework import serializers
from .models import Products,cart,Catergory
from django.contrib.auth.models import User



class Registerserializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','password','first_name', 'last_name')
		extra_kwargs = {
            'password':{'write_only': True},
        }
	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'],password = validated_data['password'],first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
		return user



class LoginSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields  = ['username','password']
		
		
class Productserializers(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = '__all__'
		
class categoryserailizers(serializers.ModelSerializer):
    
	class Meta:
		model = Catergory
		fields = '__all__'
		
		


class cartserializers(serializers.ModelSerializer):
	
	cart_user = serializers.ReadOnlyField(source = 'cart_user.username')
	items = Productserializers()
	
	class Meta:
		model = cart
		fields = "__all__"
		
	
	