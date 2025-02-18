from django.urls import path
from .views import OnboardUserView

urlpatterns = [
    path('signup/', OnboardUserView.as_view(), name='signup-user'),
]