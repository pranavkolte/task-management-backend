from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.core.mail import send_mail
from django.conf import settings
from .serializers import OnboardUserSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer

class OnboardUserView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = OnboardUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            try:
                send_mail(
                    subject='Welcome to Task Management',
                    message='Thank you for signing up for Task Management.',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
            except Exception as e:
                return Response({'detail': 'User created but failed to send email', 'error': str(e)}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    