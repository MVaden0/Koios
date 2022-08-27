class Formatting:
    colors = {
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
    }

    background_colors = {
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
    }

    formats = {
        'end'       : '\33[0m',
        'bold'      : '\33[1m',
        'italic'    : '\33[2m',
        'url'       : '\33[3m',
        'blink'     : '\33[4m',
        'blink2'    : '\33[5m',
        'selected'  : '\33[6m',
        'bold'      : '\33[7m'
    }


class Text:
    def __init__(self, text, color=None, background_color=None, formatting=None):
        self.text = text
        self.color = ''
        self.background_color = ''
        self.formatting = ''

        if color:
            self.color = Formatting.colors[color]

        if background_color:
            self.background_color = Formatting.background_colors[background_color]

        if formatting:
            self.formatting = Formatting.formats[formatting]

    def __str__(self):

        return f'{self.color}{self.background_color}{self.formatting}{self.text}{Formatting.formats["end"]}'
