from Main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'Pls work my dude....'
    assert response.status_code == 200