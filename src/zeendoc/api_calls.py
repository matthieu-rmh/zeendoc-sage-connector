import os
import requests
from dotenv import load_dotenv

def get_zeendoc_credentials() -> dict[str, str | None]: 
    """
    Get the SAGE credentials generated from the .env file
    """
    load_dotenv()
    envs = {
            "full_url": os.getenv('ZEENDOC_URL')
            }
    return envs

def make_api_request(body: dict[str, str]) -> dict:
    """
    A boilerplate used to call zeendoc api methods upon
    """
    endpoint = get_zeendoc_credentials()["full_url"]
    # As the api authenticate by using cookies, we directly use a session object
    # so that we don't bother fetching those every time 
    s = requests.Session()
    return s.post(f'{endpoint}', json=body).json()

def import_lines(mapped_sage_lines) -> dict[str, str]:
    """
    Import lines from SAGE to zeendoc
    """
    body = {"data": mapped_sage_lines}

    return make_api_request(body)


