from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, BasePermission
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ProduitsViewSet(viewsets.ModelViewSet):
	queryset = Produits.objects.all()
	serializer_class = ProduitsSerializer