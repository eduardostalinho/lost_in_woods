import random

from .player import Player
from .constants import CLANS


class Stage:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def populate(self, n_players):
        players = []
        for player in range(n_players):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            clan = random.choice(CLANS)
            players.append(Player(x, y, clan))

        return players


def check_collision(p1, p2):
    return p1.x + 1 == p2.x or p1.x - 1 == p2.x or p1.y + 1 == p2.y or p1.y - 1 == p2.y


def interact(player1, player2):
    interactions = ["FIGHT", "FRIENDLY"]
    interaction = random.choice(interactions)
