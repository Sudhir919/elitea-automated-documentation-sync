from app import app


def test_health_check_endpoint():
    """Health Check Endpoint: verify the application health endpoint."""
    """Verify the health endpoint returns a successful UP response."""
    """Verify that the health endpoint returns a successful response."""
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "UP"}
