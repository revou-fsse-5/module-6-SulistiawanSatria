def test_add_user_route(client):
    response = client.post('/add_user', json={"name": "New User", "email": "newuser@example.com"})
    assert response.status_code == 200

def test_get_users_route(client):
    response = client.get('/get_users')
    assert response.status_code == 200

def test_delete_user_route(client):
    response = client.delete('/delete_user/1')
    assert response.status_code == 200
