from parseconfig import get_base_config

class Text:
    def __init__(self, text, color=None, background_color=None, formatting=None):
        self.text = text
        self.color = ''
        self.bg_color = ''
        self.formatting = ''

        if color:
            self.color = get_base_config('colors', color)

        if background_color:
            self.background_color = get_base_config('background colors', background_color)

        if formatting:
            self.formatting = get_base_config('formats', formatting)

    def __str__(self):
        _text_formatting = f'{self.color}{self.bg_color}{self.formatting}'
        _end = get_base_config('formats', 'en')

        return f'{_text_formatting}{self.text}{_end}'
