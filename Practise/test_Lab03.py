# Put Request
# Create Token
# Create Booking ID
# URL
# Headers
# Auth - Token
# Payload

import allure
import pytest
import requests

# Create Token - Post
def create_token():
    # Creating a token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url,headers=headers,json=payload)
    token = response.json()["token"]
    return token

def create_booking():
    # Booking ID
    print("Crating a booking ID")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url,headers=headers,json=payload)
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    put_url = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload = {
        "firstname": "Abhi",
        "lastname": "J",
        "totalprice": 1211,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url = put_url,headers=headers,json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Abhi"

def test_delete():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    delete_url = url + str(booking_id)
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(headers)
    response = requests.delete(url = delete_url,headers=headers)
    assert response.status_code == 201
