import pytest
from die import Die


@pytest.fixture
# Create a Die with 6 sides
def die():
    return Die(6)

def test_die_init():
    die = Die(4)
    # Verify that the number of sides is set correctly
    assert die._Die__numberSides == 4


def test_die_init_invalid_sides():
    die = Die(1)
    # Verify that the number of sides < 2 defaults to 6 for invalid input
    assert die._Die__numberSides == 6

    # Verify that the number >100 of sides defaults to 6 for invalid input
    die = Die(120)
    assert die._Die__numberSides == 6


def test_die_roll(die):
    previous_value = die.currentValue
    new_value = die.roll()

    # Verify that the rolled value is different from the previous value
    assert new_value != previous_value
    # Verify that the rolled value is within the valid range
    assert 1 <= new_value <= die._Die__numberSides

