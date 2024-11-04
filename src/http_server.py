from flask import Flask
from services.config_service import config_blueprint

server = Flask(__name__)
server.register_blueprint(config_blueprint)

if __name__ == "__main__":
    server.run(port=5000)
