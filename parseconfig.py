import json


def get_base_config(category, key):
    with open('config.json') as file:
        # load file
        _config = json.load(file)

        # validate category
        _categories = _config.keys()
        if category not in _categories:
            raise Exception(
                f'{category} is not a valid category'
            )

        # get sub-level config based on category
        _categorical_config = _config[category]

        # validate key
        _keys = _categorical_config.keys()
        if key not in _keys:
            raise Exception(
                f'{key} is not a valid key for the category {category}'
            )

        return _categorical_config[key]