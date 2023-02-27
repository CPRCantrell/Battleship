import game_tools as gtool
from player import Player
class BattleshipGame:
    def __init__(self) -> None:
        self.player_one = Player(None)
        self.player_two = Player(None)
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.setup_players()
        # self.game_loop()
        # self.display_winner()

    def display_welcome(self):
        welcome = '''
                                                Welcome to Battleship!
                                                ----------------------
        In this game you will be placing your ships on your board trying to avoid them all being sunk. Then players
        will be taking turns calling cordnates to see if they hit or not. First person to seek all the ships wins!
        '''
        gtool.clear_screen
        print(welcome)
        input('\n\nPress Enter to continue')
        gtool.clear_line(3)

    def setup_players(self):
        self.set_names()
        print('\n\nYou will know take turns setting up your own board!\n\n')
        input('Press Enter to continue')
        gtool.clear_screen()
        self.set_boards()

    def set_names(self):
        print('\n\nFirst things first lets get your name!\n\n')
        self.player_one = Player(input('Player 1. Please input your name: '))
        self.player_two = Player(input('Player 2. Please input your name: '))

    def set_boards(self):
        input(f'First up is {self.player_one}! Press Enter When Ready!')
        gtool.clear_screen()
        self.player_one.set_ships()
        input('\n\nCOMPLETE\n\n')