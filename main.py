from email import message
import sys
import time
import os
from components import Formatting, Text, Select
from terminalutilities import *

b = Text(text="sdfsd", formatting=Formatting(color='blue', formatting='italic'))
a = Select(
    'What action would you like to perform?',
    [
        'Get information',
        'Set information',
        'Create file'
    ]
)

a.output()
#time.sleep(1.0)
#erase_last_n_rows(3)
#sys.stdout.flush()


