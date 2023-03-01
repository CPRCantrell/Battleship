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
            play_again = gtool.validate_Y_N('Would you like to play again: ')

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

        player_one = Player(self.__vadid_name__('Player 1. Please input your name: '))
        player_two = Player(self.__vadid_name__('Player 2. Please input your name: '))
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
        gtool.clear_screen()
        print(f'{self.players[0]} board:{self.players[0].board}\n')
        print(f'{self.players[1]} board:{self.players[1].board}\n')
        print(f'{f"{self.players[0]}" if self.players[1] else f"{self.players[1]}"}! You are the winner!')
        input('\n\nPress Enter to continue.')
        gtool.clear_line()

    def __need_Changes__(self,player):
        while True:
            gtool.clear_screen()
            print(f'Your Board:{player.board}')

            if gtool.validate_Y_N('Any last minute changes you want to make: '):
                gtool.clear_line()
                player.change_ship_coordinates()
            else: break

    def __vadid_name__(self, prompt):
        while True:
            user_input = input(prompt).strip()
            gtool.clear_line()
            if gtool.check_keyword(user_input):
                continue

            if user_input == '':
                print('INVALID ENTRY : You gotta put something for your name : ', end='')
                continue
            elif len(user_input) < 2:
                print('INVALID ENTRY : A single chatacter name -_- come on : ', end='')
                continue

            print(f'{prompt}{user_input.title()}')
            return user_input.title()