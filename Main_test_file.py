from Main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'Pls work......## it works now?, ye it does'
    assert response.status_code == 200