import os, sys, unittest, requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sage.api_calls import get_sage_credentials, authenticate

class TestSageApiCalls(unittest.TestCase):

    def test_sage_credentials_types(self) -> None:
        """
        Test if the .env is loaded at the root of the project
        and the env variables have been set correctly
        """
        sage_credentials = get_sage_credentials()

        self.assertIsInstance(sage_credentials["url_endpoint"], str, """
                              Endpoint not instantiated
                              """)
        self.assertIsInstance(sage_credentials["username"], str, """
                              Username not instantiated
                              """)
        self.assertIsInstance(sage_credentials["password"], str, """
                              Password not instantiated
                              """)

    def test_sage_authentication(self) -> None:
        """
        Test if we can authenticate to the sage API
        """
        session = requests.Session()
        authentication_response = authenticate(session)
        self.assertIs(authentication_response.status_code, 200, "Couldn't authentify")

if __name__ == "__main__":
    unittest.main()

