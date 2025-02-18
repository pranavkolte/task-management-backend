from django.urls import path
from .views import TaskCreateAPIView, TaskReadUpdateDeleteAPIView

urlpatterns = [
    path('', TaskCreateAPIView.as_view(), name='create-list-task'),
    path('<uuid:task_id>/', TaskReadUpdateDeleteAPIView.as_view(), name='update-delete-task'),
]