from django.shortcuts import render
from users.models import *
from users.serializers import *
from django.http import HttpResponse,response
# Create your views here.
from rest_framework import (
    generics, permissions, response, status, views, exceptions, viewsets, filters)
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
import jwt
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .permissions import *
from rest_framework.authtoken.models import Token


# Create your views here.

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class= LoginSerializer

    def post(self,request):
        data=request.data
        username = data.get('username','')
        password = data.get('password','')
        user = auth.authenticate(username=username,password=password)

        if user:
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)


            data={
                "user":serializer.data,"token":auth_token,
            }
        
            return Response(data,status=status.HTTP_200_OK)

        return Response({'detail':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)

class TeacherViewset(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    '''
    def get_queryset(self):
        students = Student.objects.all()
        return students

    
    def post(self,request,*args,**kwargs):

        students = request.data
        username = students.get('username','')
        password = students.get('password','')
        user = auth.authenticate(username=username,password=password)        
        new_stud = Student.objects.create(user=user,name=students["name"],roll_no=students["roll_no"],age = students["age"],std=students["std"],email=students["email"],contact=students["contact"])
        new_stud.save()
        serializer = StudentSerializers(new_stud)
        return Response(serializer.data)
    '''
    def get_permissions(self):    
        if self.request.method == 'POST' or self.request.method == 'DELETE':
            self.permission_classes = [Is_Teacher]
        return super(TeacherViewset, self).get_permissions()
