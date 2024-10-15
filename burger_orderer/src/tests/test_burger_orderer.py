import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_burgers_get(client):
    """Test the /api/getBurgers endpoint for successful get."""
    response = client.get('/api/getBurgers')
    assert response.status_code == 200
    assert any(burger["name"] == "Cheeseburger" for burger in response.get_json())

def test_get_specials_default_burger(client):
    """Test the /api/getSpecials endpoint for successful get."""
    response = client.get('/api/getSpecials?burger=Cheeseburger')
    assert response.status_code == 200
    assert any(special == "Add pickles" for special in response.get_json())

def test_get_specials_no_burger(client):
    """Test the /api/getSpecials endpoint for no burger."""
    response = client.get('/api/getSpecials')
    assert response.status_code == 400
    assert response.get_json() == {"error": "burger not found"}

def test_get_specials_no_burger_name(client):
    """Test the /api/getSpecials endpoint for no burger name."""
    response = client.get('/api/getSpecials?burger=')
    assert response.status_code == 400
    assert response.get_json() == {"error": "burger not found"}

def test_get_specials_non_existent_burger(client):
    """Test the /api/getSpecials endpoint for non existent burger"""
    response = client.get('/api/getSpecials?burger=taco')
    assert response.status_code == 400
    assert response.get_json() == {"error": "burger not found"}

def test_new_order_valid_data(client):
    response = client.post('/api/newOrder', json={"order": {"burger": "Cheeseburger", "specials": []}})
    assert response.data.decode('utf-8') == "success"
    assert response.status_code == 200