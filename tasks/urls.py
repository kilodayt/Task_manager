from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import TaskListCreateAPIView, TaskDetailAPIView, TaskUpdateAPIView, TaskDeleteAPIView


app_name = 'tasks'

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='tasks:schema'), name='swagger'),

    path('', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task_delete'),
]
