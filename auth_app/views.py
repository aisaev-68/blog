from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer, UserLoginSerializer


class UserRegistrationAPIView(APIView):
    """
    API регистрации пользователя.
    """

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)

        return JsonResponse({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)






class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({
                    'success': True,
                    'token': token.key,
                    'user_id': user.id,
                    'username': user.username
                })
        return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)




class UserLogoutAPIView(APIView):
    """
    API для выхода пользователя из системы.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user.auth_token)
        try:
            request.user.auth_token.delete()
            logout(request)
        except (AttributeError, ObjectDoesNotExist):
            pass  # Handle if token doesn't exist

        return Response(status=status.HTTP_200_OK)


class CurrentUserAPIView(APIView):
    """
    API для получения информации о текущем пользователе.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)