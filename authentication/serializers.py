from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'is_subscribed', 'password']
        read_only_fields = ['is_subscribed', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
