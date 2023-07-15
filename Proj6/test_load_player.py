import pytest
from load_player import load_player
from save_player import save_player
from unittest.mock import patch

@pytest.mark.parametrize(
    "name, max_hitpoints, current_hp, player_class",
    [
        ("Player1", 40, 32, "Warrior"),
        ("Player2", 30, 28, "Mugwump"),
        ("Player3", 35, 32, "Bulette"),
        ("Player4", 41, 36, "Paladin")
    ]
)


def test_load_player_yes(name, max_hitpoints, current_hp, player_class):
    # Create a sample player_data dictionary from the paramet
    player_data = {
        "name": name,
        "max-hitpoints": max_hitpoints,
        "current-hitpoints": current_hp,
        "class": player_class
    }

    # simulate an input of y(es) (to load)
    with patch('builtins.input', return_value='y'):
        save_player(name, max_hitpoints, current_hp, player_class)
        result = load_player()

    # Verify the results are the intended parameters
    assert result == (name, max_hitpoints, current_hp, player_class)


def test_load_player_no():
    # simulate an input of n(o) (to not load)
    with patch('builtins.input', return_value='n'):
        result = load_player()
    # Verify load does not load the parameters and returns None
    assert result == None
