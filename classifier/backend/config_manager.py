class ConfigManager:
    import json
    '''
    WARNING: the library looks at the pwd of the script that executes it!
    So if parent dir calls child dir ConfigManager, CM will look for config.json in parent dir
    '''
    with open('config.json') as json_file:
        data = json.load(json_file)

    @staticmethod
    def get_config():
        return ConfigManager.data
