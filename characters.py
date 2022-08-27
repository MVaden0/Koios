from email import charset


class Character:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return CHARACTERS[self.key]

CHARACTERS = {
    'right arrow': '\u2192',
    'question mark': '\u2753'
}

RIGHT_ARROW = 'U+1F816'