import pytest
from django.contrib.auth.models import User
from overdue_tasks.utils import mark_overdue_tasks
from tasks.models import Task
from datetime import timedelta
from django.utils import timezone
import django


django.setup()


@pytest.mark.django_db
def test_mark_overdue_tasks():
    user = User.objects.create_user(username='testuser', password='password')

    task1 = Task.objects.create(
        title="Test Task 1",
        description="This is a test task.",
        status="in_progress",
        due_date=timezone.now() - timedelta(days=1),
        owner=user,
    )

    task2 = Task.objects.create(
        title="Test Task 2",
        description="This is another test task.",
        status="todo",
        due_date=timezone.now() + timedelta(days=1),
        owner=user,
    )

    overdue_count = mark_overdue_tasks()

    assert overdue_count == 1
    task1.refresh_from_db()
    task2.refresh_from_db()
    assert task1.is_overdue is True
    assert task2.is_overdue is False
