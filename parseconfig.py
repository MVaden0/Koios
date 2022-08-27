import json

from exceptions import InvalidTextFormattingException


def get_base_config(category, key):
    with open('config.json') as file:
        # load file
        _config = json.load(file)

        # validate category
        _categories = _config.keys()
        if category not in _categories:
            raise InvalidTextFormattingException(
                f'\'{category}\' is not a valid category'
            )

        # get sub-level config based on category
        _categorical_config = _config[category]

        # validate key
        _keys = _categorical_config.keys()
        if key not in _keys:
            raise InvalidTextFormattingException(
                f'\'{key}\' is not a valid key for the category {category}'
            )

        # must prepend \33 escape char here, as its invalid in json
        return f'\33{_categorical_config[key]}'