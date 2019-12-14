from dataclasses import dataclass

@dataclass
class Player:
    def __init__(self, x, y, clan=None):
        self.x = x
        self.y = y
        self.clan =  clan
        self.reputation = {
            "CLAN1": 50
        }
    def move(self, direction):
        if direction == UP:
            self.y -= 1
        elif direction == DOWN:
            self.y += 1
        elif direction == LEFT:
            self.x -= 1
        elif direction == RIGHT:
            self.x += 1

