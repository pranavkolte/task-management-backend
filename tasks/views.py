from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task


class TaskCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticated] 
    
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(created_by=request.user)
        serializer = TaskSerializer(tasks, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskReadUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, task_id, *args, **kwargs):
        try:
            task = Task.objects.get(task_id=task_id)
            if not request.user.is_superuser and task.created_by != request.user:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, task_id, *args, **kwargs):
        try:
            task = Task.objects.get(task_id=task_id)
            if not request.user.is_superuser and task.created_by != request.user:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, task_id, *args, **kwargs):
        try:
            task = Task.objects.get(task_id=task_id)
            if not request.user.is_superuser and task.created_by != request.user:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    