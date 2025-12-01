import pytest
from rest_framework import status
from django.contrib.auth.models import User


@pytest.fixture
def token(client):
    user = User.objects.create_user(username='testuser', password='password')
    response = client.post('/auth/token/', {'username': 'testuser', 'password': 'password'})
    return response.data['access']


@pytest.fixture
def task_data():
    return {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'status': 'todo',
        'due_date': "2025-12-01",
    }


@pytest.mark.django_db
def test_create_task(client, token, task_data):
    response = client.post('/tasks/', task_data, HTTP_AUTHORIZATION=f'Bearer {token}')

    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert response.data['title'] == task_data['title']


@pytest.mark.django_db
def test_get_tasks(client, token, task_data):
    client.post('/tasks/', task_data, HTTP_AUTHORIZATION=f'Bearer {token}')

    response = client.get('/tasks/', HTTP_AUTHORIZATION=f'Bearer {token}')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) > 0
    assert response.data['results'][0]['title'] == task_data['title']


@pytest.mark.django_db
def test_update_task(client, token, task_data):
    response = client.post('/tasks/', task_data, HTTP_AUTHORIZATION=f'Bearer {token}')
    task_id = response.data['id']

    updated_data = {
        'title': 'Updated Task',
        'description': 'Updated description.',
        'status': 'in_progress',
        'due_date': "2025-12-01",
    }

    response = client.put(
        f'/tasks/{task_id}/update/', updated_data, HTTP_AUTHORIZATION=f'Bearer {token}', content_type='application/json'
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Updated Task'
    assert response.data['status'] == 'in_progress'


@pytest.mark.django_db
def test_delete_task(client, token, task_data):
    response = client.post('/tasks/', task_data, HTTP_AUTHORIZATION=f'Bearer {token}')
    task_id = response.data['id']

    response = client.delete(f'/tasks/{task_id}/delete/', HTTP_AUTHORIZATION=f'Bearer {token}')

    assert response.status_code == status.HTTP_204_NO_CONTENT
