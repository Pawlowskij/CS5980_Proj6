import json
import pytest
from save_player import save_player
@pytest.mark.parametrize(
    "name, max_hitpoints, current_hp, player_class",
    [
        ("Player1", 30, 30, "Warrior"),
        ("Player2", 20, 20, "Mugwump"),
        ("Player3", 50, 50, "Paladin"),
        ("Player4", 60, 60, "Bulette"),
    ]
)
def test_save_player(name, max_hitpoints, current_hp, player_class):
    # Call the function to be tested
    save_player(name, max_hitpoints, current_hp, player_class)

    # Load the saved JSON file
    with open("player_save.json") as infile:
        saved_data = json.load(infile)

    # Assert the saved data matches the expected values
    assert saved_data["name"] == name
    assert saved_data["max-hitpoints"] == max_hitpoints
    assert saved_data["current-hitpoints"] == current_hp
    assert saved_data["class"] == player_class