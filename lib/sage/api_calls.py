import requests
from pathlib import Path
import json

# Get the endpoint URL from the config.json file
def get_endpoint_url():
    config_path = Path(__file__).parent.parent.parent / "config.json"
    with open(config_path, 'r') as file:
        config = json.load(file)
        return config['endpoint']

def get_receipt_lines():
    endpoint = get_endpoint_url()
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
    endpoint = get_endpoint_url()
    response = session.get(f'{endpoint}/$connect?username=sage&password=')
