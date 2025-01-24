import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the 'Hello, World!' response from the root URL."""
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200
