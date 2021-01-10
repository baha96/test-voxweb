from django.contrib.auth import authenticate, login
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from account import serializers


class RegisterView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Пользователь успешно создан."
            },
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        user = authenticate(request, username=cd['username'].lower(), password=cd['password'])
        if user is not None:
            serializer = serializers.ProfileDetailSerializer(instance=user)
            login(request, user)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "wrong_email_or_password"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )


class ProfileEditView(generics.UpdateAPIView):
    permission_classes = (
        # IsAuthenticated,
    )
    serializer_class = serializers.ProfileEditSerializer

    def put(self, request, *args, pk=None, **kwargs):
        try:
            user = User.objects.get(
                pk=pk,
                is_active=True,
            )
            self.check_object_permissions(request, user)
            serializer = self.serializer_class(
                data=request.data,
                instance=user,
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    'message': 'ok'
                },
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    'message': 'not_found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class MyProfileGetView(generics.RetrieveAPIView):
    """Получить свой профиль при обновление страницы"""
    permission_classes = ()
    serializer_class = serializers.ProfileDetailSerializer

    def get(self, request, *args, pk=None, **kwargs):
        try:
            user = User.objects.get(
                pk=request.user.pk,
                is_active=True,
            )
            self.check_object_permissions(request, user)
            serializer = self.serializer_class(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
