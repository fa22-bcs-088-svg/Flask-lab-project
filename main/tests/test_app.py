from app import app
import json

client = app.test_client()

def test_home_route():
    response = client.get('/')
    assert response.status_code == 200

def test_health_route():
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_quiz_post_correct_data():
    test_data = {
        "answers": {
            "1": "Paris",
            "2": "JavaScript",
            "3": "Cascading Style Sheets"
        }
    }
    response = client.post('/data', json=test_data)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["score"] == 3
