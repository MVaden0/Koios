from email import message
import sys
import time
import os
from color import Color


class List:
    def __init__(self, prompt, answers):
        self.prompt = prompt
        self.answers = answers

    def draw(self):
        print(f'{Color.red}{self.prompt}{Color.end}')

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


print(f'{Color.red}test{Color.end}')
print(f'{Color.black}test{Color.end}')
print(f'{Color.green}test{Color.end}')
print(f'{Color.yellow}test{Color.end}')
print(f'{Color.blue}test{Color.end}')
print(f'{Color.violet}test{Color.end}')
print(f'{Color.beige}test{Color.end}')
print(f'{Color.white}test{Color.end}')
print(f'{Color.grey}test{Color.end}')
print(f'{Color.red2}test{Color.end}')
print(f'{Color.green2}test{Color.end}')
print(f'{Color.yellow2}test{Color.end}')
print(f'{Color.blue2}test{Color.end}')
print(f'{Color.violet2}test{Color.end}')
print(f'{Color.beige2}test{Color.end}')
print(f'{Color.white2}test{Color.end}')
print(f'{Color.red}{Color.selected}test{Color.end}')
print(f'{Color.red}{Color.blink}test{Color.end}')
print(f'{Color.red}test{Color.end}')
