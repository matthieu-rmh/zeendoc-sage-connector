import os, sys
from redis_om import Migrator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.config import Config

def get_config_by_id(id):
    return Config.find(Config.id == id).first()
    

def config_service_eval():
    Migrator().run()
    res = get_config_by_id(0)
    print(str(res))

if __name__ == "__main__":
    config_service_eval()
