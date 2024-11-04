import os, sys
from flask import Blueprint, jsonify, request
from redis_om import Migrator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.config import Config

config_blueprint = Blueprint('config_blueprint', __name__)

@config_blueprint.route('/configs', methods=['GET'])
def get_configs():
    Migrator().run()
    res = jsonify([ conf.__dict__ for conf in Config.find().all()])
    print(type(res))
    return res

@config_blueprint.route('/configs/<int:config_id>', methods=['GET'])
def get_config(config_id: int):
    Migrator().run()
    return Config.find(Config.id == config_id).first().__dict__

@config_blueprint.route('/configs', methods=['POST'])
def create_config():
    Migrator().run()
    config_data_request_body = request.json
    creating_config = Config(**config_data_request_body)

    creating_config.save()
    created_config = Config.find(Config.id == config_data_request_body["id"]).first().__dict__ 
    return jsonify(created_config), 201


@config_blueprint.route('/configs/<int:config_id>/update', methods=['PUT'])
def update_config(config_id: int):
    Migrator().run()
    initial_config_fields_dict = Config.find(Config.id==config_id).first().__dict__
    change_parameters_dict = request.json
    applied_parameters_dict = initial_config_fields_dict | change_parameters_dict 

    updated_config = Config(**applied_parameters_dict)
    updated_config.save()
    return jsonify(updated_config.__dict__, 200)

@config_blueprint.route('/configs/<int:config_id>/delete', methods=['DELETE'])
def delete_config(config_id: int):
    Migrator().run()
    config_to_be_deleted = Config.find(Config.id == config_id).first()
    config_to_be_deleted.delete(config_to_be_deleted.pk)

    return "config deleted", 201

def config_service_eval():
    Migrator().run()
    print("simple eval of this module")

if __name__ == "__main__":
    config_service_eval()
