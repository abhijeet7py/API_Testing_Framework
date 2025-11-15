import pytest
import allure
import requests

@allure.title("Test GET Request- Restful Booker")
@allure.description("TC#1- Verify that GET request with a ID works")
@allure.tag("regression","P0","smoke")
@allure.label("owner","Abhijeet")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_byid_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 200
    print(response_data.json())
    print(response_data.cookies)
    print(response_data.headers)

@allure.title("Test GET Request- Restful Booker")
@allure.description("TC#2- Verify that GET request with a -ID Throws an error")
@allure.tag("regression","P0","smoke")
@pytest.mark.smoke
def test_get_single_request_byid_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404

@allure.title("Test GET Request- Restful Booker")
@allure.description("TC#3- Verify that GET request with a invalid ID Throws an error")
@allure.tag("regression","P0","smoke")
@pytest.mark.smoke
def test_get_single_request_byid_negative_2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404


