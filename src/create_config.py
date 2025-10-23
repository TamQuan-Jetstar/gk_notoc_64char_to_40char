from pathlib import Path
import json
import datetime
import os
import sys

def create_config(env: str):
    # get path to this location and find config_files from there so that this code works when compiled to exe
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_path, "config_files", f"{env}.config.json")   

    # names of config files all follow the same format with "dev", "prd", "test"
    with open(json_path, 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    
    timestamp = datetime.datetime.now()
    year = timestamp.year
    month = timestamp.month
    day = timestamp.day
    hour = timestamp.hour
    minute = timestamp.minute
    second = timestamp.second

    logger = {}
    logger['log_folder'] = Path(config_data['logger']['folder_location'] + f"\\YEAR_{year}\\MONTH_{month}\\DAY_{day}\\HOUR_{hour}")
    logger['log_filename'] = f"GK_NOTOC_LOGS_MIN_{minute}_SECOND_{second}"

    notoc = {}
    notoc['archive'] = Path(config_data['notoc_folder']['archive'])
    notoc['source'] = Path(config_data['notoc_folder']['source'])
    notoc['destination'] = Path(config_data['notoc_folder']['destination'])

    config = {}
    config['logger'] = logger
    config['notoc'] = notoc
    
    return config
        