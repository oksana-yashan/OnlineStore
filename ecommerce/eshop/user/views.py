from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import UserSerializer, UserSerializerWithToken
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
    pagination_class=None
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
    

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, user_id):
    user = User.objects.get(id=user_id)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['is_admin']

    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


