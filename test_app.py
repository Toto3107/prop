from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Mode: not set | Secret: no secret" in response.data

