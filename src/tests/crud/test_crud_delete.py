import allure
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrappers import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class TestCrudDelete:

    @pytest.mark.delete
    @allure.title("Test CRUD Operations- Delete")
    @allure.description("Test CRUD Operations - Create-> Delete -> Get")
    def test_crud_create_delete(self,create_token,get_booking_id):
        delete_url = APIConstants.put_patch_delete_url(booking_id=get_booking_id)
        response = delete_request(
            url = delete_url,
            auth= None,
            headers= Utils().common_header_put_delete_patch_cookie(token=create_token),
            in_json= False
        )
        # verification
        verify_status_code(response_data=response,expected_data=201)

    def test_get_deleted_request(self,create_token,get_booking_id):
        get_url = APIConstants.put_patch_delete_url(booking_id=get_booking_id)
        response = get_request(
            url= get_url,
            auth= None
        )
        verify_status_code(response_data=response,expected_data=404)
