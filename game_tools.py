import os
import sys

def clear_screen():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

def clear_line(lines = 1):
    for line in range(lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
