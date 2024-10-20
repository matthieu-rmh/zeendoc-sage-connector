import os
import requests
from dotenv import load_dotenv

def get_sage_credentials() -> dict[str, str | None]: 
    """
    Get the SAGE credentials generated from the .env file
    """
    load_dotenv()
    return {
            "url_endpoint": os.getenv('SAGE_ENDPOINT'),
            "username": os.getenv('SAGE_USERNAME'),
            "password": os.getenv('SAGE_PASSWORD')
            }

def get_receipt_lines():
    endpoint = get_sage_credentials()["url_endpoint"]
    # As the api authenticate by using cookies, we directly use a session object
    # so that we don't bother fetching those every time 
    s = requests.Session()
    authenticate(s)
    # sample parameters used to fetch receipt lines
    body = {
        "dateRef": "2023-01-01",
        "Societe": "Société 1"
    }
    response = s.post(f'{endpoint}/CET_CAPI/GetReceptions', json=body)
    parsed_response = response.json()
    return parsed_response

def authenticate(session):
    # Here the endpoint url should be like
    endpoint = get_sage_credentials()["url_endpoint"]
    username = get_sage_credentials()["username"]
    password = get_sage_credentials()["password"]
    response = session.get(f'{endpoint}/$connect?username={username}&password={password}')
