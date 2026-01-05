import allure
import pytest
import requests

@allure.title("Test GET Request - Fake store API")
@allure.description("TC1 - Verify that GET Request works- Positive")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_user():
    url = "https://fakestoreapi.com/users/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    print(response_data.status_code)
    print(response_data.json())
    assert response_data.status_code == 200

@allure.title("Test GET Request - Fake store API")
@allure.description("TC2 - Verify that GET Request works- Negative")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_user_negative():
    url = "https://fakestoreapi.com/users/invalid"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 400