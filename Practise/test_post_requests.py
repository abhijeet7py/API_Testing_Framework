import allure
import pytest
import requests

@allure.title("TC- Add a new user")
@allure.description("Verify Add a new user")
@pytest.mark.crud
def test_add_new_user():
    # To make request
    # URL
    # Method - Post
    # Headers
    # Payload/ Data/ Body - json/Dict
    # Auth - No

    base_url = "https://fakestoreapi.com"
    path = "/users"
    url = base_url + path
    headers = {"Content-Type": "application/json"}
    payload = {"username": "john_doe",
                "email": "john@example.com",
                 "password": "pass123"
               }

    response = requests.post(url = url, headers= headers, json = payload)

    assert response.status_code == 201

    response_data = response.json()

    id = response_data["id"]
    assert id > 0
    assert id is not None
    assert type(id) == int

@allure.title("TC- Add a new user Negative")
@allure.description("Verify Add a new user")
@pytest.mark.crud
def test_add_new_user_negative():
    base_url = "https://fakestoreapi.com"
    path = "/users"
    url = base_url + path
    headers = {"Content-Type": "application/json"}
    payload = {}

    response = requests.post(url= url, headers=headers,json=payload)

    assert response.status_code == 500
