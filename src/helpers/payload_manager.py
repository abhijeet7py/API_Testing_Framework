# Payloads

def payload_create_booking():
    payload = {
    "firstname": "Abhijeet",
    "lastname": "Jathar",
    "totalprice": "2341",
    "depositpaid": "true",
    "bookingdates": {
        "checkin": "2025-04-21",
        "checkout": "2025-04-25"
    },
    "additionalneeds": "Breakfast"
}
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload