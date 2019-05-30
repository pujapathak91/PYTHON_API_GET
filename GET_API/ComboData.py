import requests
import json
import unittest
import ProjectConfig


# Initialize Base URL
base_URL = ProjectConfig.intialize_appurl()


class ComboData(unittest.TestCase):

    def test_get__specific_user_and_album_Response(self):
        # Send GET request for 5th users
        response_5th_user = requests.get(base_URL+"/users/5")

        # Send GET request for 50th albums
        response_50th_album = requests.get(base_URL+"/albums/50")

        # Display Response content for 5th user & 50th album
        print("Response data for user : ")
        print(json.dumps(response_5th_user.json(),indent=4))
        print("Response data for album : ")
        print(json.dumps(response_50th_album.json(), indent=4))


if __name__ == '__main__':
    unittest.main()
