import game_tools as gtool
from boats import *

class Board():
    def __init__(self) -> None:
        self.board = [[' ']*10 for col in range(10)]
        self.translate = {
            'col': {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9},
            'row': {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9}
        }
        self.boats = [AircraftCarrier(),Battleship(),Submarine(),Destroyer()]

    def prep_board(self):
        unset_boat = self.boats
        self.boats = []
        self.__set_ships__(unset_boat)
        gtool.clear_screen()
        print(f'\n\n{self}\n')

    def __set_ships__(self,unset_boat):
        while len(unset_boat) != 0:
            gtool.clear_screen()
    #prints board
            print(f'\n\n{self}\n')
    #print boat name and size (w/ 'O')
            for boat in unset_boat:
                print(f'{boat} - {"O"*boat.length}')
    #set ship cordnates on board
            next_boat = unset_boat.pop(0)
            print(f'\nWhere do you want to put the {next_boat}?')
            next_boat.body_cordnates.extend(self.__collect_cordinates__(next_boat.length))
            self.boats.append(next_boat)

    def __collect_cordinates__(self, length):
        col = [key for key in self.translate['col'].keys()]
        row = [key for key in self.translate['row'].keys()]
        while True:
            starting_cord, direction = self.__validate_entries__(col,row)
            cords = [starting_cord]
            try:
                return self.__add_ship_to_board__(cords, direction, col, row, length)
            except: print('Does not fit! Try another spot')

    def __validate_entries__(self,col_valid,row_valid):
        dir_valid = ['RIGHT', 'DOWN']
        cordnate, direction = input('\nPlease type a starting cordinate and either if you want it to go down or right from that point.\nExample: A9 RIGHT : ').upper().split()
        while cordnate[0] not in col_valid:
            cordnate[0] = input(f'Invalid column. Only the following entries are allowed: {col_valid} : ').upper()
        while cordnate[1] not in row_valid:
            cordnate[1] = input(f'Invalid column. Only the following entries are allowed: {row_valid} : ').upper()
        while direction not in dir_valid:
            direction = input(f'Invalid column. Only the following entries are allowed: {dir_valid} : ').upper()
        return cordnate, direction

    def __add_ship_to_board__(self,cords, direction, col, row, length):
        while len(cords) < length:
            add_cord = ''
            if direction == 'RIGHT':
                for column in range(len(col)):
                    if cords[-1][0] == col[column]:
                        add_cord += col[column+1]
                        break
                add_cord += cords[0][1:]
            else:
                add_cord += cords[0][0]
                for num_row in range(len(row)):
                    if cords[-1][1:] == row[num_row]:
                        add_cord += row[num_row+1]
                        break
            if len(add_cord) <= 1:
                raise Exception()
            cords.append(add_cord)
        for cordinates in cords:
            if self.board[self.translate['row'][cordinates[1:]]][self.translate['col'][cordinates[0]]] == ' ':
                self.board[self.translate['row'][cordinates[1:]]][self.translate['col'][cordinates[0]]] = 'O'
            else:
                raise Exception()
        return cords

    def __str__(self) -> str:
        row_num = 1
        board = f'{"Your Board":>18}\n   A B C D E F G H I J\n'
        for row in self.board:
            if row_num < 10:
                board += str(f'{row_num} |{"|".join(row)}|\n')
            else:
                board += str(f'{row_num}|{"|".join(row)}|')
            row_num += 1
        return board

board = Board()
print(board)
input('ready')
board.prep_board()