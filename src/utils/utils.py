# contains common utilities
# Setting headers
# Read data from a excel file
# read data from the csv, json file
# Set the headers

class Utils:

    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass