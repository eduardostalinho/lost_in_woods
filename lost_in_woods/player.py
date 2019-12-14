import random
from .constants import UP, LEFT, DOWN, RIGHT

FIGHT = "FIGHT"
FRIENDLY = "FRIENDLY"
INTERACTIONS = [FIGHT, FRIENDLY]

MOVING = "MOVING"
INTERACTING = "INTERACTING"
STATUSES = [MOVING, INTERACTING]


class Player:
    def __init__(self, x, y, clan=None):
        self.x = x
        self.y = y
        self.clan = clan
        self.status = (MOVING,)

    def move(self, direction):
        if direction == UP:
            self.y -= 1
        elif direction == DOWN:
            self.y += 1
        elif direction == LEFT:
            self.x -= 1
        elif direction == RIGHT:
            self.x += 1

    def interact(self, other):
        interaction = random.choice(INTERACTIONS)
        self.status = INTERACTING, interaction, other
