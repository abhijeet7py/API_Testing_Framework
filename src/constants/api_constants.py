# API Constants - Class which contains all the endpoints
# Keep the URLS

class APIConstants:
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def create_auth_url(self):
        return "https://restful-booker.herokuapp.com/auth"

    def create_booking_url(self):
        return "https://restful-booker.herokuapp.com/booking"

    def put_patch_delete_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)