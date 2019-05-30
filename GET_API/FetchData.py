import requests
import json
import unittest
import ProjectConfig


# Initialize Base URL
base_URL = ProjectConfig.intialize_appurl()


class FetchData(unittest.TestCase):


    def test_get_User_Response(self):
        # Send GET request for /users
        response_users = requests.get(base_URL+"/users")

        # Check Total number of Response Json for /users
        total_users = len(response_users.json())
        print("Total number of users present: " + str(total_users))
        self.assertTrue(total_users == 10, "Total number of user is matching")

        # Display Response content for /users
        print("Response data for users: ")
        print(json.dumps(response_users.json(),indent=4))

    def test_get_Album_Response(self):
        # Send GET request for /Albums
        response_album = requests.get(base_URL + "/albums")

        # Display Total number of Response Json for /Albums
        total_albums = len(response_album.json())
        print("Total number of users present: " + str(total_albums))
        self.assertTrue(total_albums == 100)


if __name__ == '__main__':
    unittest.main(verbosity=2)
