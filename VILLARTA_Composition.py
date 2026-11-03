class Room:
    def __init__(self, name: str):
        self.name = name

class House: 
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

my_house = House()
for room in my_house.rooms:
    print(f"Room created: {room.name}")