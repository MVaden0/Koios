class Color:
    end      = '\33[0m'
    bold     = '\33[1m'
    italic   = '\33[3m'
    url      = '\33[4m'
    blink    = '\33[5m'
    blink2   = '\33[6m'
    selected = '\33[7m'

    black    = '\33[30m'
    red      = '\33[31m'
    green    = '\33[32m'
    yellow   = '\33[33m'
    blue     = '\33[34m'
    violet   = '\33[35m'
    beige    = '\33[36m'
    white    = '\33[37m'

    black_bg  = '\33[40m'
    red_bg    = '\33[41m'
    green_bg  = '\33[42m'
    yellow_bg = '\33[43m'
    blue_bg   = '\33[44m'
    violet_bg = '\33[45m'
    beige_bg  = '\33[46m'
    white_bg  = '\33[47m'

    grey    = '\33[90m'
    red2    = '\33[91m'
    green2  = '\33[92m'
    yellow2 = '\33[93m'
    blue2   = '\33[94m'
    violet2 = '\33[95m'
    beige2  = '\33[96m'
    white2  = '\33[97m'

    grey_bg    = '\33[100m'
    red_bg2    = '\33[101m'
    green_bg2  = '\33[102m'
    yellow_bg2 = '\33[103m'
    blue_bg2   = '\33[104m'
    violet_bg2 = '\33[105m'
    beige_bg2  = '\33[106m'
    white_bg2  = '\33[107m'


class Formatting:
    end         = '\33[0m'
    bold        = '\33[1m'
    italic      = '\33[2m'
    url         = '\33[3m'
    blink       = '\33[4m'
    blink2      = '\33[5m'
    selected    = '\33[6m'
    bold        = '\33[7m'


class Text:
    def __init__(self, text, color=None, formatting=None):
        self.text = text
        self.color = ''
        self.formatting = ''

        if color:
            self.color = color

        if formatting:
            self.formatting = formatting

    def __str__(self):
        return f'{self.color}{self.formatting}{self.text}{Formatting.end}'
