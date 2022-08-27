from readchar import readkey, key
import sys

from config import get_config
from terminalutilities import erase_last_n_rows, hide_cursor, show_cursor, move_cursor_up, move_cursor_down


class Formatting:
    def __init__(self, color=None, background_color=None, formatting=None):
        self.color = ''
        self.background_color = ''
        self.formatting = ''

        if color:
            self.color = get_config('colors', color)

        if background_color:
            self.background_color = get_config('background colors', background_color)

        if formatting:
            self.formatting = get_config('formats', formatting)

    def apply(self, text):
        _text_formatting = f'{self.color}{self.background_color}{self.formatting}'
        _end = get_config('formats', 'end')

        return f'{_text_formatting}{text}{_end}'


class Text:
    def __init__(
            self, 
            text, 
            formatting=Formatting()
        ):
        self.text = text
        self.formatting = formatting

    def output(self):
        print(self.formatting.apply(self.text))

class Select:
    def __init__(
            self, 
            prompt, 
            answers, 
            prompt_formatting=Formatting(color='violet', formatting='bold'), 
            answer_formatting=Formatting(color='grey'), 
            selected_formatting=Formatting(color='cyan')
        ):
        self.prompt = prompt
        self.answers = answers
        self.answer_count = len(answers)
        self.selected_index = 0
        self.prompt_formatting = prompt_formatting
        self.answer_formatting = answer_formatting 
        self.selected_formatting = selected_formatting

    def _output(self):
        print(self.prompt_formatting.apply(self.prompt))

        for i in range(0, len(self.answers)):
            if i == self.selected_index:
                print(self.selected_formatting.apply(f' > {self.answers[i]}'))

            else:
                print(self.answer_formatting.apply(f'   {self.answers[i]}'))

        move_cursor_up(1)

    def output(self):
        hide_cursor()

        self._output()

        while(True):
            _action = readkey()

            if _action == key.ENTER:
                move_cursor_down(1)

                break

            elif _action == key.UP:
                erase_last_n_rows(3)

                if self.selected_index == 0:
                    self.selected_index = self.answer_count - 1
                
                else:
                    self.selected_index -= 1

                self._output()

            elif _action == key.DOWN:
                erase_last_n_rows(3)

                if self.selected_index == self.answer_count - 1:
                    self.selected_index = 0
                
                else:
                    self.selected_index += 1

                self._output()
                
        show_cursor()