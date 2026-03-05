def test_app_health(client):
    """
    This test uses the 'client' fixture from conftest.py
    to check if the FastAPI app boots up correctly.
    """
    response = client.get("/")  # Or whatever your home route is
    assert response.status_code == 200