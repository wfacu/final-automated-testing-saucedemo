import requests


BASE_URL = "https://reqres.in/api"


def test_create_user():

    payload = {
        "name": "Facundo",
        "job": "QA Automation"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Facundo"
    assert body["job"] == "QA Automation"

    assert "id" in body
    assert "createdAt" in body