from django.urls import path
from .views import OnboardUserView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('signup/', OnboardUserView.as_view(), name='signup-user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login-user'),
    path("refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
]