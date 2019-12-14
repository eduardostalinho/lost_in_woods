from lost_in_woods import Stage
from lost_in_woods.constants import CLANS


def test_stage_width_and_height():
    width = 100
    height = 120
    stage = Stage(width, height)
    assert stage.width == width
    assert stage.height == height


def test_populate_with_players():
    width = 100
    height = 120
    stage = Stage(width, height)

    players = stage.populate(1)

    assert len(players) == 1
    assert players[0].clan in CLANS
    assert players[0].x in range(width)
    assert players[0].x in range(height)
