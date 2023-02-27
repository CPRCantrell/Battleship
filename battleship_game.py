class BattleshipGame:
    def __init__(self) -> None:
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.setup_players()
        self.game_loop()
        self.display_winner()

    def display_welcome(self):
        print('')