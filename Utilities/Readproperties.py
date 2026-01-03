import json
import os

class ReadConfig:
    _config_data = None
    @staticmethod
    def _load_config():
        if ReadConfig._config_data is None:
            current_dir = os.path.dirname(__file__)
            config_path = os.path.join(current_dir, "config.json")
            with open(config_path, 'r') as file:
                ReadConfig._config_data = json.load(file)
        return ReadConfig._config_data

    @staticmethod
    def getBaseurl():
        return ReadConfig._load_config().get('baseUrl')
