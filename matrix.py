import shutil
import time
import random

COLUMN, ROW = shutil.get_terminal_size()

COLORS = [
  '\033[32;1m', # GREEN
  '\033[37;1m', # WHITE
  '\033[36;1m', # CYAN
  '\033[34m' # BLUE
]
END_COLOR = '\033[0m'
CHARS = [chr(i) for i in range(ord('A'), ord('z'))]

def print_line():
    for i in range(COLUMN):
        color = random.choice(COLORS)
        char = random.choice(CHARS)

        if random.random() < 0.5:
            print(color + char + END_COLOR, end='')
        else:
            print(' ', end='')

    print(flush=True)

while True:
    print_line()
    time.sleep(0.1);
