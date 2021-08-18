from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import transaction
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework.response import Response


class ProduitsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Produits
		fields="__all__"

class TokenPairSerializer(TokenObtainPairSerializer):
	
	def validate(self,attrs):
		data = super(TokenPairSerializer,self).validate(attrs)
		data['is_admin'] = self.user.is_superuser
		data['groups'] = [x.name for x in self.user.groups.all()]
		data['username'] = self.user.username
		data['first_name'] = self.user.first_name
		data['last_name'] = self.user.last_name

		return data

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		read_only_fields = "is_active","is_staff",
		exclude = "last_login","is_staff","date_joined","user_permissions",

		extra_kwargs = {
			'username':{
				'validators=[UnicodeUsernameValidator()]',
			}
		}