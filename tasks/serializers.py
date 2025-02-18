from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True, allow_null=True)
    assigned_user_email = serializers.EmailField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'status', 'created_at', 
                 'assigned_user', 'assigned_user_email']
        optional_fields = ['assigned_user_email']
        read_only_fields = ['task_id', 'created_at', 'created_by']

    def create(self, validated_data):
        assigned_user_email = validated_data.pop('assigned_user_email', None)
        assigned_user = None
        if assigned_user_email:
            assigned_user = User.objects.get(email=assigned_user_email)
        
        request = self.context.get('request')
        user = request.user if request else None
        
        task = Task.objects.create(
            assigned_user=assigned_user,
            created_by=user,
            **validated_data
        )
        return task

    def update(self, instance, validated_data):
        if 'assigned_user_email' in validated_data:
            assigned_user_email = validated_data.pop('assigned_user_email')
            instance.assigned_user = User.objects.get(email=assigned_user_email) if assigned_user_email else None
        return super().update(instance, validated_data)
    