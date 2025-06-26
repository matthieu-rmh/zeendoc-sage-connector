from sage.api_calls import get_sage_credentials, get_receipt_lines
from core_logics import get_sage_receipt_lines, convert_receipt_lines
from models.config_pg import ConfigModel
# pg parts
from flask import jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def main():
    '''
    Main thread of our logic, where we call the corresponding functions
    to call the APIs whether from Sage or Zeendoc
    '''

    print(str(get_receipt_lines()))
    # engine = create_engine('postgresql://postgres:postgres@localhost:5433/ynit_connector')
    # Session = sessionmaker(bind=engine)
    # session = Session()
    #
    # configs = session.query(ConfigModel).all()
    # # print(jsonify(configs))
    # jsonified = [{k: v for k, v in vars(config).items() if not k.startswith('_')} for config in configs]
    # print(jsonified)

    # for config in configs:
    #     print(config.id, config.cupboard, config.enabled)
    #
    raw_sage_receipt_lines = get_sage_receipt_lines()
    # print(str(type(raw_sage_receipt_lines)))
    converted_sage_receipt_lines = convert_receipt_lines(raw_sage_receipt_lines) 

    print(str(converted_sage_receipt_lines))
    print(str(len(converted_sage_receipt_lines)))

    # this is a variable populated with mock data simulating receipt lines
    # receipts = get_sage_receipt_lines()

if __name__ == "__main__":
    main()
