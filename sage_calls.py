import requests
import json

# Get the endpoint URL from the config.json file
def get_url():
    with open('config.json', 'r') as file:
        config = json.load(file)
        return config['url']

def get_receipts():
    url = get_url()
    response = requests.get(f'{url}/receptions')
    parsed_response = response.json()
    return parsed_response

def authenticate():
    # Here the endpoint url should be 
    # http://srv-sage-smart-1000.smartenergies.local:8085/webservices/server/sdata
    # /$connect
    # but url will be provided
    print("authenticate")
