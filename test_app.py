from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"hello de" in response.data

# <-- Add this blank line so the file ends with a newline