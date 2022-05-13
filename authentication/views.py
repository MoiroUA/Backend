from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer


# Create your views here.
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email=data['email'],
            password=data['password']
        )

        login(request, user=user)

        return redirect('/auth/users/')


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'email'
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})

        serializer_data = {
            'email': user_data.get('email', request.user.email),

            'profile': {
                'first_name': user_data.get('first_name', request.user.profile.first_name),
                'last_name': user_data.get('last_name', request.user.profile.last_name),
            }
        }

        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
