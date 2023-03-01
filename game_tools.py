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

def check_keyword(user_input):
    key = user_input.upper().strip()
    if key == 'QUIT':
        return __quit_game__()
    return False

def __quit_game__():
    if validate_Y_N('Are you sure you want to quit the game: '):
        clear_screen()
        sys.exit()
    else:
        clear_line()
        return True

def validate_Y_N(prompt):
    user_input = 'playerplayer'
    valid_yes = ['YES', 'YAS', 'YUP', 'YEP', 'YEA', 'Y', 'INDEED', 'I DO', 'QUIT']
    valid_no = ['NO', 'NOPE', 'NAH', 'N', 'I AM GOOD','I\'M GOOD']

    print()
    while user_input not in valid_yes and user_input not in valid_no:
        clear_line()
        user_input = input(prompt).upper()
        if check_keyword(user_input):
            continue
        if user_input not in valid_yes and user_input not in valid_no:
            print(f'Invalid Entry: Valid entry: [Y,N] : ',end='')

    if user_input in valid_yes:
        return True
    else:
        return False