from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from datetime import datetime


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.account.models import (
    CustomUser,
    UserProfile,
    ManagerProfile,
    )

from .serializers import (
    UserSerializer,
    ManagerSerializer
    )


class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class ManagerRegisterView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    '''          
    try:
                  validated_data = serializer.validated_data
                  validated_data.pop('password2')
                  user = CustomUser(**validated_data)
                  user.set_password(validated_data.get('password'))
                  serializer.save()

                  return Response(
                      serializer.data,
                      status=status.HTTP_201_CREATED
                  )
              except Exception as ex:
                  return Response(
                      data={"error": f"User creation failed: {str(ex)}"},
                      status=status.HTTP_400_BAD_REQUEST
                  )
  '''

    '''
    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                validated_data = serializer.validated_data
                user_data = validated_data.pop('user')
                role = user_data.pop('role')

                # role = validated_data.pop('role')
                user = CustomUser.objects.create_user(role=role, **validated_data)
                # manager = ManagerProfile(user=user, **validated_data)
                user.set_password(validated_data.get('password'))
                user.save()


                manager_profile = ManagerProfile.create(user=user, **validated_data)
                manager_profile.save()

                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as ex:
                return Response(
                    data={"error": f"User creation failed: {str(ex)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
'''