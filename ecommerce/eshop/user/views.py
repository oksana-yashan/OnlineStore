from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import UserProfileSerializer, UserSerializer, UserSerializerWithToken
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CurrentUserProfile(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
        
    def get(self, request): 
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
        
    def put(self, request):
        user = request.user
        serializer = UserSerializerWithToken(user, many=False)
        data = request.data

        user.first_name = data['name']
        user.username = data['email']
        user.email = data['email']
        
        if data['password'] != '':
            user.password = make_password(data['password'])
        user.save()
        return Response(serializer.data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]

    def get_search_fields(self, view, request):
        return request.GET.getlist("search_fields", [])

class RegisterUser(APIView):

    def post(self, request):
        data = request.data
        try:
            user = User.objects.create(
                first_name=data["name"],
                username=data['email'],
                email = data['email'],
                password=make_password(data['password'])
            )
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail':'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['POST'])
# def registerUser(request):
#     data = request.data
#     user = User.objects.create(
#             first_name=data["name"],
#             username=data['email'],
#             email = data['email'],
#             password=make_password(data['password'])
#         )
#     serializer =  UserSerializerWithToken(user, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getCurrentUserProfile(request):
#     user = request.user
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser,]
    def get_search_fields(self, view, request):
        return request.GET.getlist("search_fields", [])


class UserProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.kwargs.get("user_id"))
