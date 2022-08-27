from exceptions import InvalidTextFormattingException


def get_base_config(category, key):
    # validate category
    _categories = BASE_CONFIG.keys()
    if category not in _categories:
        raise InvalidTextFormattingException(
            f'\'{category}\' is not a valid category'
        )

    # get sub-level config based on category
    _categorical_config = BASE_CONFIG[category]

    # validate key
    _keys = _categorical_config.keys()
    if key not in _keys:
        raise InvalidTextFormattingException(
            f'\'{key}\' is not a valid key for the category {category}'
        )

    # must prepend \33 escape char here, as its invalid in json
    return f'{_categorical_config[key]}'
    

BASE_CONFIG = {
    'colors': {
        'black'         : '\33[30m',
        'grey'          : '\33[90m',
        'red'           : '\33[91m',
        'green'         : '\33[92m',
        'yellow'        : '\33[93m',
        'blue'          : '\33[94m',
        'violet'        : '\33[95m',
        'cyan'          : '\33[96m',
        'white'         : '\33[97m',
        'dark red'      : '\33[31m',
        'dark green'    : '\33[32m',
        'dark yellow'   : '\33[33m',
        'dark blue'     : '\33[34m',
        'dark violet'   : '\33[35m',
        'dark cyan'     : '\33[36m',
        'dark white'    : '\33[37m'
    },
    'background colors': {
        'black'         : '\33[40m',
        'grey'          : '\33[100m',
        'red'           : '\33[101m',
        'green'         : '\33[102m',
        'yellow'        : '\33[103m',
        'blue'          : '\33[104m',
        'violet'        : '\33[105m',
        'beige'         : '\33[106m',
        'white'         : '\33[107m',
        'dark red'      : '\33[41m',
        'dark green'    : '\33[42m',
        'dark yellow'   : '\33[43m',
        'dark blue'     : '\33[44m',
        'dark violet'   : '\33[45m',
        'dark beige'    : '\33[46m',
        'dark white'    : '\33[47m'
    },
    'formats': {
        'end'           : '\33[0m',
        'bold'          : '\33[1m',
        'italic'        : '\33[3m',
        'url'           : '\33[4m',
        'blink'         : '\33[5m',
        'blink2'        : '\33[6m',
        'selected'      : '\33[7m'
    }
}