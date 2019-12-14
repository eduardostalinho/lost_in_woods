from lost_in_woods.player import Player, MOVING, INTERACTING, INTERACTIONS
from lost_in_woods.constants import UP, DOWN, LEFT, RIGHT


def test_player_has_position_xy():
    x = 0
    y = 1
    player = Player(x, y)
    assert player.x == x
    assert player.y == y
    assert player.clan is None
    assert player.status == (MOVING,)


def test_player_move_up():
    player = Player(0, 0)
    player.move(UP)
    assert player.y == -1
    assert player.x == 0


def test_player_move_down():
    player = Player(0, 0)
    player.move(DOWN)
    assert player.y == 1
    assert player.x == 0


def test_player_move_right():
    player = Player(0, 0)
    player.move(RIGHT)
    assert player.y == 0
    assert player.x == 1


def test_player_move_left():
    player = Player(0, 0)
    player.move(LEFT)
    assert player.y == 0
    assert player.x == -1


def test_start_interaction():
    player = Player(0, 0)
    other_player = Player(1, 0)
    player.start_interaction(other_player)
    assert player.status[0] == INTERACTING
    assert player.status[1] in INTERACTIONS
    assert player.status[2] == other_player
