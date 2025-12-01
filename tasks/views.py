from django_filters import FilterSet, DateFilter, ChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer


class TaskFilter(FilterSet):
    status = ChoiceFilter(choices=Task.STATUS_CHOICES)
    due_date_after = DateFilter(field_name='due_date', lookup_expr='gte')
    due_date_before = DateFilter(field_name='due_date', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['status', 'due_date_after', 'due_date_before']


class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)


class TaskUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)


class TaskDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)
