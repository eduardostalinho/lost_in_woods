import random

from .player import Player
from .constants import CLANS


class Stage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.players = []

    def populate(self, n_players):
        for player in range(n_players):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            clan = random.choice(CLANS)
            self.players.append(Player(x, y, clan))

        return self.players

    def collisions(self):
        collisions = [
            (p1, p2)
            for i, p1 in enumerate(self.players)
            for p2 in self.players[i:]
            if self.check_collision(p1, p2)
        ]
        return collisions

    def check_collision(self, p1, p2):
        return any(
            [
                (p1.x + 1 == p2.x),
                (p1.x - 1 == p2.x),
                (p1.y + 1 == p2.y),
                (p1.y - 1 == p2.y),
            ]
        )
