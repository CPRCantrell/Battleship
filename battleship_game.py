import game_tools as gtool
from player import Player
class BattleshipGame:
    def __init__(self) -> None:
        self.players = []
        self.run_game()

    def run_game(self):
        play_again = True
        while play_again:
            self.display_welcome()
            self.setup_players()
            self.game_loop()
            self.display_winner()
            play_again = self.__validate_Y_N__('Would you like to play again: ')

    def display_welcome(self):
        welcome = '''
                                                Welcome to Battleship!
                                                ----------------------
        In this game you will be placing your ships on your board trying to avoid them all being sunk. Then players
        will be taking turns calling cordnates to see if they hit or not. Your turn ends only when you miss. First
        person to seek all the ships wins!
        '''
        gtool.clear_screen()
        print(welcome)
        input('\n\nPress Enter to continue')
        gtool.clear_line(3)

    def setup_players(self):
        self.set_names()
        print('\n\nYou will know take turns setting up your own board!\n\n')
        input('Press Enter to continue')
        gtool.clear_screen()
        self.set_boards()
        input('\n\nEverything is all set. Press Enter to play.')

    def set_names(self):
        print('\n\nFirst things first lets get your name!\n\n')

        player_one = Player(input('Player 1. Please input your name: ').title())
        player_two = Player(input('Player 2. Please input your name: ').title())
        self.players = [player_one,player_two]

    def set_boards(self):
        for player in self.players:
            input(f'{player}! Press Enter When Ready!')
            gtool.clear_screen()
            player.place_all_ships()
            self.__need_Changes__(player)
            gtool.clear_screen()

    def game_loop(self):
        game_over = False
        input(f'{self.players[0]} your up first. Press Enter when ready!')
        turn = 0
        while not game_over:
            gtool.clear_screen()
            player = self.players[turn%2]
            turn += 1
            opponent = self.players[turn%2]

            while player.strike(opponent):
                input('Nice hit! You go again! Press Enter to continue')
                if opponent.living():
                    break

            if opponent.living():
                game_over = True
            else:
                input('Sorry that\'s a miss! Press Enter to clear screen and continue.')
                gtool.clear_screen()
                input(f'The turn is now being passed over to {opponent}. {opponent}, when you are ready press enter.')

    def display_winner(self):
        gtool.clear_line()
        print(f'{self.players[0]} board:{self.players[0].board}\n')
        print(f'{self.players[1]} board:{self.players[1].board}\n')
        print(f'{f"{self.players[0]}" if self.players[1] else f"{self.players[1]}"}! You are the winner!')
        input('\n\nPress Enter to continue.')
        gtool.clear_line()

    def __need_Changes__(self,player):
        while True:
            gtool.clear_screen()
            print(f'Your Board:{player.board}')

            if self.__validate_Y_N__('Any last minute changes you want to make: '):
                gtool.clear_line()
                player.change_ship_coordinates()
            else: break

    def __validate_Y_N__(self,prompt):
            user_input = 'playerplayer'
            valid_yes = ['YES', 'YUP', 'YEA', 'Y', 'INDEED', 'I DO']
            valid_no = ['NO', 'NOPE', 'Na', 'N', 'I AM GOOD']

            print()
            while user_input not in valid_yes and user_input not in valid_no:
                user_input = input(prompt).upper()
                gtool.clear_line()
                if user_input not in valid_yes and user_input not in valid_no:
                    print(f'Invalid Entry: Valid entry: [Y,N] : ',end='')

            if user_input in valid_yes:
                return True
            else:
                return False