from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

from account import models


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}
    )
    username = serializers.CharField(
        max_length=100, required=True,
    )
    first_name = serializers.CharField(
        max_length=100, required=True,
    )
    last_name = serializers.CharField(
        max_length=100, required=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "warning": "Пароли не совпадают"
            })
        password2 = data['password2']
        password_validation.validate_password(password2)

        return data

    def create(self, validated_data):
        user = User.objects.filter(username=validated_data['username']).exists()

        if user:
            raise serializers.ValidationError({
                "warning": "Данный email уже зарегистрирован в системе."
            })
        else:
            user = User(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
    )


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            'user_django',
        )


class ProfileDetailSerializer(serializers.ModelSerializer):
    additional = UserProfileDetailSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
            'additional',
        )


class ProfileEditSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=False, style={'input_type': 'password'}, allow_blank=True
    )
    first_name = serializers.CharField(
        max_length=100, required=True,
    )
    last_name = serializers.CharField(
        max_length=100, required=True,
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'password',
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
