from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserProfileDataSerializer

# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):  
                user = serializer.save()
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "success": True,
                    "message": "User registered successfully.",
                    "data": {
                        "Token": token.key,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "username": user.username,
                        "email": user.email,
                    },
                }, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            response_data = {
                "success": False,
                "message": None
            }
            if 'email' in e.detail:
                response_data["message"] = e.detail['email'][0]
            elif 'username' in e.detail:
                response_data["message"] = e.detail['username'][0]
            else:
                response_data["message"] = "Invalid data provided."
            
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            token, _=Token.objects.get_or_create(user=user)
            return Response({
                    "success": True,
                    "message": "User logged-in successfully.",
                    "data": {
                        "Token": token.key,
                    },
                }, status=status.HTTP_201_CREATED)
        
        return Response({"success":False, "message":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserProfileDataView(APIView):
    def post(self, request, username):
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['user'] = user.username

        serializer = UserProfileDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)