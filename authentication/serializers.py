from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('Email is required to log in')

        if password is None:
            raise serializers.ValidationError('A password is required to log in')

        user = authenticate(email=email, password=password)

        if not user.is_active:
            raise serializers.ValidationError('User has been deactivated')

        return {
            'email': user.email,
            'password': user.password
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)
    # profile = ProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        ordering = ['first_name', 'last_name']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        profile_data = validated_data.pop('profile', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password()
        instance.save()

        for key, value in profile_data.items():
            setattr(instance.profile, key, value)
        instance.save()

        return instance



