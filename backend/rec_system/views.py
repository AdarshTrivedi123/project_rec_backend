from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer

# Create your views here.
class RegisterAPIView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token, _=Token.objects.get_or_create(user=user)
            return Response({"Token":token.key},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            token, _=Token.objects.get_or_create(user=user)
            return Response({"Token":token.key},status=status.HTTP_201_CREATED)
        
        return Response({"error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)