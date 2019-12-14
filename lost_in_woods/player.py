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
        self.health_points = 10

    def act(self):
        if self.status[0] == "MOVING":
            self.move(random.choice([UP, LEFT, RIGHT, DOWN]))
        elif self.status[0] == "INTERACTING":
            self.interact(self.status[1], self.status[2])

    def interact(self, interaction, player):
        if interaction == FIGHT:
            self.fight(player)
        if interaction == FRIENDLY:
            self.make_friend(player)

    def make_friend(self, other_player):
        pass

    def fight(self, other_player):
        other_player.health_points -= 1

    def move(self, direction):
        if direction == UP:
            self.y -= 1
        elif direction == DOWN:
            self.y += 1
        elif direction == LEFT:
            self.x -= 1
        elif direction == RIGHT:
            self.x += 1

    def start_interaction(self, other):
        interaction = random.choice(INTERACTIONS)
        self.status = INTERACTING, interaction, other
        other.status = INTERACTING, interaction, self
