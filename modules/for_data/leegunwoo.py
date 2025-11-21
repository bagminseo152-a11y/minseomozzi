from sonjiho import *
import json

def get_json_from_file(dir):
    with open(f"./DB/{dir}", 'r', encoding='utf-8') as f:
        return json.load(f)


def write_file_from_json(json_data, dir):
    with open(f"./DB/{dir}", 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_data, indent=4, ensure_ascii=False))


def get_params(**params):
    base_params = {
        'serviceKey': service_key,       
        'MobileOS': 'ETC',               
        'MobileApp': 'AppTest',          
        '_type': 'json',
    }

    for k, v in params.items():
        base_params[k] = v

    return base_params