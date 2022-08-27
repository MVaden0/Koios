import sys
import os
from turtle import clear
import time

def move_cursor_to_home():
    sys.stdout.write('\x1b[H')

def move_cursor_to_position(row, col):
    sys.stdout.write(f'\x1b[{row};{col}H')

def move_cursor_up(rows):
    sys.stdout.write(f'\x1b[{rows}A')

def move_cursor_down(rows):
    sys.stdout.write(f'\x1b[{rows}B')

def move_cursor_right(cols):
    sys.stdout.write(f'\x1b[{cols}C')

def move_cursor_left(cols):
    sys.stdout.write(f'\x1b[{cols}D')

def move_cursor_beginning_of_next_line_down(rows):
    sys.stdout.write(f'\x1b[{rows}E')

def move_cursor_beginning_of_next_line_up(rows):
    sys.stdout.write(f'\x1b[{rows}F')

def move_cursor_to_col(col):
    sys.stdout.write(f'\x1b[{col}G')

def erase_cursor_to_end_of_screen():
    sys.stdout.write(f'\x1b[0j')

def erase_cursor_to_beginning_of_screen():
    sys.stdout.write(f'\x1b[1j')

def erase_cursor_to_end_of_line():
    sys.stdout.write(f'\x1b[0k')

def erase_start_of_line_to_cursor():
    sys.stdout.write(f'\x1b[1k')

def erase_line():
    sys.stdout.write(f'\x1b[2k')

def erase_last_n_rows(rows): 
    sys.stdout.write(f'\x1b[{rows}A')
    sys.stdout.write('\x1b[0J')
