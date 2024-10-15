import pytest
from ..src.main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_sum_numbers(client):
    """Test the /api/sum endpoint for valid input."""
    response = client.post('/api/sum', json={'a': 3, 'b': 4})
    assert response.status_code == 200
    assert response.get_json()['result'] == 7

def test_sum_numbers_missing_parameters(client):
    """Test the /api/sum endpoint for missing parameters."""
    response = client.post('/newOrder', json={"order": { "burger": "test burger", "specials": [] }})
    assert response.status_code == 200
    assert response.get_text() == "success"