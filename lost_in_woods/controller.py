from .stage import Stage
from itertools import chain

stage = Stage(20, 20)
players = stage.populate(10)


def run():
    for player in players:
        stage.collisions()
        for collision in stage.collisions():
            collision[0].start_interaction(collision[1])
        player.act()
        if player.status[0] == "INTERACTING" and player not in chain(
            [p[0] for p in stage.collisions()], [p[1] for p in stage.collisions()]
        ):
            player.status = ("MOVING",)
        print((player.x, player.y), player.status, player.health_points)
        if player.health_points <= 0:
            stage.players.remove(player)
