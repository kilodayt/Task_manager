from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .utils import mark_overdue_tasks


class RecalculateOverdueTasksAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        updated_count = mark_overdue_tasks()
        return Response(
            {'message': f'Обновлено {updated_count} просроченных задач'},
            status=status.HTTP_200_OK
        )
