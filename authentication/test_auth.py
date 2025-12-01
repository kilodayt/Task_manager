import pytest
from rest_framework import status
from django.contrib.auth.models import User
import django


django.setup()


@pytest.mark.django_db
def test_get_jwt_tokens(client):
    user = User.objects.create_user(username='testuser', password='password')

    response = client.post('/auth/token/', {'username': 'testuser', 'password': 'password'})

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_invalid_login(client):
    response = client.post('/auth/token/', {'username': 'invalid', 'password': 'invalid'})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.data