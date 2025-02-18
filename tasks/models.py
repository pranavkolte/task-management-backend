import uuid

from django.conf import settings
from django.db import models


class Task(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        choices=[('todo', 'To-Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
        default='todo',
        max_length=20
    )
    priority = models.CharField(
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        default='medium',
        max_length=20
    )
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'task'
