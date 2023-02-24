class Boats:
    def __init__(self,name:str, length:int) -> None:
        self.name = name
        self.length = length
        self.body_cordnates = []

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