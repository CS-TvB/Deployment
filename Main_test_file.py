from Main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'It finaly works jaaayy!!'
    assert response.status_code == 200