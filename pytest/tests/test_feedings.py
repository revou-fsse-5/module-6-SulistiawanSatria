def test_get_feedings(client):
    response = client.get('/feedings')
    assert response.status_code == 200

def test_add_feeding(client):
    data = {"animal_id": 1, "enclosure_id": 2, "food_type": "Banana", "feeding_time": "2024-10-11T12:00:00"}
    response = client.post('/feedings', json=data)
    assert response.status_code == 200
