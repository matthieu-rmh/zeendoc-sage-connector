import os
import requests
from dotenv import load_dotenv

def get_sage_credentials() -> dict[str, str | None]: 
    """
    Get the SAGE credentials generated from the .env file
    """
    load_dotenv()
    envs = {
            "url_endpoint": os.getenv('SAGE_ENDPOINT'),
            "username": os.getenv('SAGE_USERNAME'),
            "password": os.getenv('SAGE_PASSWORD'),
            "society": os.getenv('SAGE_SOCIETY')
            }
    return envs

def make_api_request(method: str, body: dict[str, str]) -> dict:
    """
    A boilerplate used to call sage api methods upon
    """
    endpoint = get_sage_credentials()["url_endpoint"]
    # As the api authenticate by using cookies, we directly use a session object
    # so that we don't bother fetching those every time 
    s = requests.Session()
    authenticate(s)
    return s.post(f'{endpoint}{method}', json=body).json()


def get_receipt_lines() -> dict[str, str]:
    """
    Get receipt lines from SAGE
    """
    body = {
        "dateRef": "2023-01-01",
        "Societe": "Société 1"
    }

    return make_api_request("/CET_CAPI/GetReceptions", body)

def authenticate(session: requests.Session) -> requests.Response:
    credentials = get_sage_credentials()
    endpoint = credentials["url_endpoint"]
    username = credentials["username"]
    password = credentials["password"]
    society = credentials["society"]
    return session.get(f'{endpoint}/$connect?username={username}&password={password}&society={society}')
