import pytest
from django.test import Client
from django.urls import reverse

@pytest.fixture
def client():
    return Client()

def test_admin_login(client):
    response = client.get(reverse('admin:login'))
    assert response.status_code == 200