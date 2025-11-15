import allure
import pytest
import requests

@allure.title("TC#1- Create Booking CRUD Positive")
@allure.description("TC#1- Verify Create Booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Headers
    # Auth
    # Payload
    # Method
    base_url = "https://restful-booker.herokuapp.com"
    path_param = "/booking"
    url = base_url + path_param
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Abhijeet",
        "lastname": "Jathar",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-10-11",
            "checkout": "2025-10-15"
        },
        "additionalneeds": "Breakfast"
    }
    # Method
    response = requests.post(url, headers= headers,json=payload)
    # Status code verification
    assert response.status_code == 200
    # Response body verification
    response_data = response.json()
    bookingid = response_data["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_data["booking"]["firstname"]
    lastname = response_data["booking"]["lastname"]
    totalprice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]
    checkin = response_data["booking"]["bookingdates"]["checkin"]
    checkout = response_data["booking"]["bookingdates"]["checkout"]

    assert firstname == "Abhijeet"
    assert lastname == "Jathar"
    assert totalprice == 123
    assert depositpaid == True
    assert checkin == "2025-10-11"
    assert checkout == "2025-10-15"

@allure.title("TC#2- Create booking crud negative")
@allure.description("TC#2- Verify create booking with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    path_param = "/booking"
    url = base_url + path_param
    headers = {"Content-Type": "application/json"}
    payload = {}
    response_data = requests.post(url,headers=headers,json=payload)
    print(type(url))
    print(type(headers))
    print(type(payload))

    assert response_data.status_code == 500

@allure.title("TC#3- Create Booking CRUD Negative")
@allure.description("TC#3- Verify Create booking with totalprice negative")
@pytest.mark.crud
def test_create_booking_negative_tc3(): # This has bug response should be 401
    base_url = "https://restful-booker.herokuapp.com"
    path_param = "/booking"
    url = base_url + path_param
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Abhijeet",
        "lastname": "Jathar",
        "totalprice": -123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-10-11",
            "checkout": "2025-10-15"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url, headers=headers,json=payload)
    assert response_data.status_code == 200

