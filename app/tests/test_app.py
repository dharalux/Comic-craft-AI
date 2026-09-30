from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_homepage():

    response = client.get("/")

    assert response.status_code == 200

    assert "ComicCraft" in response.text


def test_docs():

    response = client.get("/docs")

    assert response.status_code == 200


def test_openapi():

    response = client.get("/openapi.json")

    assert response.status_code == 200