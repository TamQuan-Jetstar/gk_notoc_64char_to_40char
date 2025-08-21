from pathlib import Path
import json


def create_config(env: str):
    with open(f"src/{env}.config.json", 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    logger = {}
    logger['log_folder'] = Path(config_data['logger']['folder_location'])
    logger['log_filename'] = config_data['logger']['file_name']

    notoc = {}
    notoc['archive'] = Path(config_data['notoc_folder']['archive'])
    notoc['source'] = Path(config_data['notoc_folder']['source'])
    notoc['destination'] = Path(config_data['notoc_folder']['destination'])

    config = {}
    config['logger'] = logger
    config['notoc'] = notoc

    return config
