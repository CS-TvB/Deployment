from Main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'Pls ffs do some work'
    assert response.status_code == 200