from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('services/', include('overdue_tasks.urls', namespace='overdue_tasks')),
]
