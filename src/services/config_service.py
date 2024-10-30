import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import config

def this_test():
    this_config = config.Config(id=1, cupboard=78)
    print(str(this_config))

if __name__ == "__main__":
    this_test()
