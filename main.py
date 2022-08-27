from email import message
import sys
import time
import os
from text import Text


class List:
    def __init__(self, prompt, answers):
        self.prompt = prompt
        self.answers = answers

    def draw(self):
        print(f'{self.prompt}')

        for answer in self.answers:
            print(answer)

q = List(
    prompt='What action will you like to perform?',
    answers=[
        'Get information',
        'Set information',
        'Overwrite file'
    ]
)

q.draw()

a = Text(text="hello!!!", color='red')
print(a)