from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
    OVERDUE = 'overdue'

    STATUS_CHOICES = [
        (TODO, 'TO DO'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (OVERDUE, 'Overdue')

    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=TODO)
    due_date = models.DateField()
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_overdue = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {str(self.status)}'

