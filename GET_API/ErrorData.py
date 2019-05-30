import requests
import json
import unittest
import ProjectConfig

# Initialize Base URL
base_URL = ProjectConfig.intialize_appurl()


class ErrorData(unittest.TestCase):

    def test_get_Error_User_Response(self):
        # Send GET request for 11th users
        response_users = requests.get(base_URL+"/users/11")

        # Check Response for 11th /users
        total_users = len(response_users.json())
        print("Total number of users is more than zero")
        self.assertFalse(len(response_users.json()) > 0)

    def test_get_Error_Album_Response(self):
        # Send GET request for /Albums
        response_album = requests.get(base_URL + "/albums/115")

        # Check Response for 115th /Albums
        total_users = len(response_album.json())
        print("Total number of albums is more than zero")
        self.assertFalse(len(response_album.json()) > 0)


if __name__ == '__main__':
    unittest.main()
