from board import Board

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.my_board = Board()
        self.enemy_board = Board()

    def strike(self, player):
        pass

    def set_ships(self):
        self.my_board.prep_board()

    def __str__(self) -> str:
        return self.name