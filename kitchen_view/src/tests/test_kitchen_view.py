import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_new_order_success(client):
    """Test the /newOrder endpoint for successful order."""
    response = client.post('/newOrder', json={"order": { "burger": "test burger", "specials": [] }})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "success"

def test_new_order_broken_order(client):
    """Test the /newOrder endpoint for broken order."""
    response = client.post('/newOrder', json={})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_broken_burger(client):
    """Test the /newOrder endpoint for a broken burger entry"""
    response = client.post('/newOrder', json={"order": { "tacos": "test tacos", "specials": [] }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_malformed_burger_data(client):
    """Test the /newOrder endpoint for a malformed burger data. Not a string"""
    response = client.post('/newOrder', json={"order": { "burger": 123, "specials": [] }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_empty_burger_data(client):
    """Test the /newOrder endpoint for a empty burger data."""
    response = client.post('/newOrder', json={"order": { "burger": "", "specials": [] }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_broken_specials(client):
    """Test the /newOrder endpoint for a broken specials entry"""
    response = client.post('/newOrder', json={"order": { "burger": "test burger", "you are my specialz": [] }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_malformed_specials(client):
    """Test the /newOrder endpoint for a malformed specials entry. Not a list"""
    response = client.post('/newOrder', json={"order": { "burger": "test burger", "specials": 123 }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"

def test_new_order_malformed_specials_data(client):
    """Test the /newOrder endpoint for a malformed specials data. Not a string"""
    response = client.post('/newOrder', json={"order": { "burger": "test burger", "specials": [123, None] }})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "error"
