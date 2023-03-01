from board import Board
import game_tools as gtool

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.board = Board()
        self.lost = False
        self.strike_history = []

    def strike(self, opponent):
        gtool.clear_screen()
        print(f'Your Board:{self.board}\n')
        print(f'Opponent\'s board:{opponent.board.obscure()}\n')
        coord = None
        while True:
            row, col = self.__verify_coords__('What coordinates would you like to strike: [Ex. A10]: ')
            coord = f'{col}{row}'
            if coord not in self.strike_history:
                self.strike_history.append(coord)
                break
            print(f'You have choosen {coord} before: provide another coordinate: ',end='')

        hit = opponent.board.hit_ship(coord, True)
        if hit:
            opponent.board.mark_board(coord, 'X')
        else:
            opponent.board.mark_board(coord, '-')
        return hit

    def living(self):
        life = self.board.any_sinks()
        if life == 4:
            self.lost = True
            return self.lost
        return self.lost

    def place_all_ships(self):
        for boat in range(len(self.board.boats)):
            current_boat = self.board.boats[boat]

            gtool.clear_screen()
            print(f'Your Board:{self.board}\n')
            for size in range(boat,len(self.board.boats)):
                print('O'*self.board.boats[size].length, f' - {self.board.boats[size]}')

            print()
            while True:
                row, col = self.__verify_coords__(f'Select a coordinate for your {current_boat}: [Ex. A10] : ')
                direction = self.__verify_direction__(f'From {col}{row}, which out of the 4 directions do you want your {current_boat} to go: [Ex. Left] : ')

                try: self.board.set_boat_coords(boat, row, col, direction)
                except:
                    print('Invadid Entry: Ship does not fit: ',end='')
                    continue

                for coord in self.board.boats[boat].body_coordinates:
                    self.board.mark_board(coord, 'O')
                break

    def change_ship_coordinates(self):
        index = 1
        print()
        for boat in self.board.boats:
            print(f'{index}) {boat}')
            index += 1

        print()
        while index not in [0,1,2,3]:
            try: index = (int(input('Which boat would you like to change: '))-1)
            except:
                gtool.clear_line()
                print('Invalid Entry: Valid entries are: [0,1,2,3] : ',end='')
            if index not in [0,1,2,3]:
                gtool.clear_line()
                print('Invalid Entry: Valid entries are: [0,1,2,3] : ',end='')

        gtool.clear_screen()
        print(f'Your Board:{self.board}\n')
        current_boat = self.board.boats[index]
        print('O'*current_boat.length, f' - {current_boat}')
        self.board.clear_ship(index)

        print()
        while True:
            row, col = self.__verify_coords__(f'Select a coordinate for your {current_boat}: [Ex. A10] : ')
            direction = self.__verify_direction__(f'From {col}{row}, which out of the 4 directions do you want your {current_boat} to go: [Ex. Left] : ')

            try: self.board.set_boat_coords(index, row, col, direction)
            except:
                print('Invadid Entry: Ship does not fit: ',end='')
                continue

            for coord in current_boat.body_coordinates:
                self.board.mark_board(coord, 'O')

            break

    def clear_board(self):
        self.board.clear_board()

    def __str__(self) -> str:
        return self.name

    def __verify_coords__(self,prompt):
        while True:
            key = False
            user_input = input(prompt).strip()
            gtool.clear_line()
            if gtool.check_keyword(user_input):
                    continue

            while user_input == '' or len(user_input)<2 or len(user_input)>3:
                user_input = input(f'Invade Entry: {prompt}').strip()
                gtool.clear_line()
                if gtool.check_keyword(user_input):
                    key = True
                    break

            col = user_input[0].upper()
            row = user_input[1:]

            while col not in self.board.col:
                col = input(f'[{col}] is an invalid column. Enter one of the following : {self.board.col} : ')
                gtool.clear_line()
                if gtool.check_keyword(user_input):
                    key = True
                    break

            while row not in self.board.row:
                row = input(f'[{row}] is an invalid row. Enter one of the following : {self.board.row} : ')
                gtool.clear_line()
                if gtool.check_keyword(user_input):
                    key = True
                    break

            if key: continue
            return row, col

    def __verify_direction__(self, prompt):
        while True:
            key = False
            user_input = input(prompt).upper().strip()
            gtool.clear_line()
            valid_directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']

            if gtool.check_keyword(user_input):
                continue

            while user_input not in valid_directions:
                user_input = input(f'Invade Entry: {prompt}').upper()
                gtool.clear_line()
                if gtool.check_keyword(user_input):
                    key = True
                    break

            if key: continue
            return user_input
