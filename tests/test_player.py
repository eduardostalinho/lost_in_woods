from lost_in_woods import Player


def test_player_has_position_xy():
    x = 0
    y = 1
    player = Player(x, y)
    assert player.x == x
    assert player.y == y
    assert player.clan is None

def test_player_move_up():
    player = Player(0, 0)
    player.move('UP')
    assert player.y == -1
    assert player.x == 0


def test_player_move_down():
    player = Player(0, 0)
    player.move('DOWN')
    assert player.y == 1
    assert player.x == 0


def test_player_move_right():
    player = Player(0, 0)
    player.move('RIGHT')
    assert player.y == 0
    assert player.x == 1

def _test_player_move_left():
    player = Player(0, 0)
    player.move('LEFT')
    assert player.y == 0
    assert player.x == -1