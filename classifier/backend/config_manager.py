class ConfigManager:
    import json

    with open('config.json') as json_file:
        data = json.load(json_file)

    @staticmethod
    def get_config():
        return ConfigManager.data
