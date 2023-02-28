import game_tools as gtool
from boats import *

class Board():
    def __init__(self) -> None:
        self.board = [[' ']*10 for row in range(10)]
        self.col = ['A','B','C','D','E','F','G','H','I','J']
        self.row = ['1','2','3','4','5','6','7','8','9','10']
        self.boats = [AircraftCarrier(),Battleship(),Submarine(),Destroyer()]

    def set_boat_coords(self, boat, row, col, direction):
        coord_list = [f'{col}{row}']
        more_coords = self.boats[boat].length-1
        self.boats[boat].body_coordinates = []

        if direction == 'UP' or direction == 'DOWN':
            start_point_index = int(row)-1
            if direction == 'UP':
                for coord in range(more_coords):
                    start_point_index -= 1
                    if start_point_index < 0:
                        raise Exception()
                    coord_list.append(f'{col}{self.row[start_point_index]}')
            elif direction == 'DOWN':
                for coord in range(more_coords):
                    start_point_index += 1
                    coord_list.append(f'{col}{self.row[start_point_index]}')

        if direction == 'RIGHT' or direction == 'LEFT':
            for index in range(len(self.col)):
                if col == self.col[index]:
                    start_point_index = index
                    break
            if direction == 'RIGHT':
                for coord in range(more_coords):
                    start_point_index += 1
                    coord_list.append(f'{self.col[start_point_index]}{row}')
            elif direction == 'LEFT':
                for coord in range(more_coords):
                    start_point_index -= 1
                    if start_point_index < 0:
                        raise Exception()
                    coord_list.append(f'{self.col[start_point_index]}{row}')

        for coord in coord_list:
            if self.hit_ship(coord):
                raise Exception()

        self.boats[boat].body_coordinates = coord_list

    def hit_ship(self,coord, ship_being_struck = False):
        for boat in self.boats:
            if not boat.sunk:
                if boat.hit(coord, ship_being_struck):
                    return True
        return False

    def any_sinks(self):
        num_of_sinks = 0
        for boat in self.boats:
            if boat.sunk:
                num_of_sinks +=1
        return num_of_sinks


    def mark_board(self,coordinate:str, marking):
            col = coordinate[0]
            for index in range(len(self.col)):
                if col == self.col[index]:
                    col = index
                    break
            row = int(coordinate[1:])-1
            self.board[row][col] = marking

    def obscure(self):
        row_num = 1
        board = f'\n   {" ".join(self.col)}\n'
        for row in self.board:
            if row_num < 10:
                board += f'{row_num} |'
            else:
                board += f'{row_num}|'
            for col in row:
                if col != 'O':
                    board += f'{col}|'
                else:
                    board += ' |'
            if row_num < 10:
                board += '\n'
            row_num += 1
        return board

    def clear_board(self):
        for row in range(len(self.board)):
            for col in range(len(row)):
                self.board[row][col] = ' '

    def clear_ship(self, index):
        coordinate = self.boats[index].body_coordinates
        for coord in coordinate:
            col = coord[0]
            for index in range(len(self.col)):
                if col == self.col[index]:
                    col = index
                    break
            row = int(coord[1:])-1
            self.board[row][col] = ' '

    def __str__(self) -> str:
        row_num = 1
        board = f'\n   {" ".join(self.col)}\n'
        for row in self.board:
            if row_num < 10:
                board += str(f'{row_num} |{"|".join(row)}|\n')
            else:
                board += str(f'{row_num}|{"|".join(row)}|')
            row_num += 1
        return board