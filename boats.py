import game_tools as gtool
class Boats:
    def __init__(self,name:str, length:int) -> None:
        self.name = name
        self.length = length
        self.body_coordinates = []
        self.health = length
        self.sunk = False

    def hit(self, coord, ship_being_struck = False):
        for hit in self.body_coordinates:
            if coord == hit:
                if ship_being_struck:
                    self.health -= 1
                    if self.health == 0:
                        self.sunk = True
                        input(f'You sunk my {self}!!')
                        gtool.clear_line()
                return True
        return False

    def __str__(self) -> str:
        return self.name.title()

class Destroyer(Boats):
    def __init__(self) -> None:
        super().__init__('destroyer', 2)

class Submarine(Boats):
    def __init__(self) -> None:
        super().__init__('submarine', 3)

class Battleship(Boats):
    def __init__(self) -> None:
        super().__init__('battleship', 4)

class AircraftCarrier(Boats):
    def __init__(self) -> None:
        super().__init__('aircraft carrier', 5)