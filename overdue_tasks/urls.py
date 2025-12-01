from django.urls import path
from .views import RecalculateOverdueTasksAPIView


app_name = 'overdue_tasks'

urlpatterns = [
    path('recalculate_overdue/', RecalculateOverdueTasksAPIView.as_view(), name='recalculate_overdue'),
]
