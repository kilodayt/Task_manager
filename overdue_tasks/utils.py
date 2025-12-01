from django.utils import timezone
from tasks.models import Task


def mark_overdue_tasks():
    now = timezone.now()
    overdue_tasks = Task.objects.filter(due_date__lt=now, is_overdue=False).exclude(status='done')

    return overdue_tasks.update(is_overdue=True)
