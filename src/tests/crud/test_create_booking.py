# API testcase
# URL -> API_Constants.py
# headers -> Utils.py
# payload -> payload_manager
# HTTP Post -> api_request_wrapper
# verification -> common_verification.py
from logging import Logger

import allure
import pytest
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.api_requests_wrappers import post_request
from src.helpers.common_verifications import *
import logging

class TestCreateBooking:

    @allure.title("Verify that create Booking status and ID shouldn't be null")
    @allure.description("Creating a Booking from a Payload and verify that ID shouldn't be null and status code == 200")
    @pytest.mark.positive
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase - TC1 - positive")
        response = post_request(
            url= APIConstants().create_booking_url(),
            auth = None,
            headers = Utils().common_headers_json(),
            payload = payload_create_booking(),
            in_json= False
        )
        verify_status_code(response_data=response,expected_data=200)
        verify_json_key_for_notnull(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("Ending the Testcase - TC1 - positive")

    @allure.title("Verify that create Booking doesn't work with no payload")
    @allure.description("Creating a Booking with no payload and verify that booking id")
    @pytest.mark.negative
    def test_create_booking_negative(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase - TC2 - negative")
        response = post_request(
            url = APIConstants().create_booking_url(),
            auth = None,
            headers= Utils().common_headers_json(),
            payload= {},
            in_json= False
        )
        verify_status_code(response_data=response,expected_data=500)