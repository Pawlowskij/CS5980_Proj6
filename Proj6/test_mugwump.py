import pytest

from mugwump import Mugwump
from die import Die

# create fixture mugwump
@pytest.fixture
def my_mugwump():
    mugwump = Mugwump(1)
    d10 = Die(10)

    # artificially set max hitpoints
    mugwump.maxHitPoints = 20
    mugwump.hitPoints = 20
    return mugwump

# test that mugwump HP is same as the Max HP at initialization
def test_Mugwump_hitpoints():
    # Create a Mugwump object
    mugwumpHP = Mugwump(1)
    assert mugwumpHP.maxHitPoints == mugwumpHP.hitPoints
    # Test that HP is between 6 and 60
    assert mugwumpHP.maxHitPoints >= 6 and mugwumpHP.maxHitPoints <= 60


def test_take_damage(my_mugwump):
    # check for damage of 5 resulting in 15
    my_mugwump.takeDamage(5)
    assert (my_mugwump.hitPoints == 15)

    # overheal should return max HP
    my_mugwump.takeDamage(-100)
    assert (my_mugwump.hitPoints == 20)

    # overkill should return 0 HP
    my_mugwump.takeDamage(2000000)
    assert (my_mugwump.hitPoints == 0)

    # Test valid attack choice
def test_attackChoice(monkeypatch, my_mugwump):
    # Simulate user input '1' for claws attack
    monkeypatch.setattr('builtins.input', lambda _: '1')
    choice = my_mugwump.attackChoice()
    assert choice == 1

    # Simulate user input '2' for fangs attack
    monkeypatch.setattr('builtins.input', lambda _: '2')
    choice = my_mugwump.attackChoice()
    assert choice == 2

    # Simulate user input '3' for heals attack
    monkeypatch.setattr('builtins.input', lambda _: '3')
    choice = my_mugwump.attackChoice()
    assert choice == 3

    # # Test invalid attack choice -- creates an infinite loop because of While True in attackChoice??
    # monkeypatch.setattr('builtins.input', lambda _: '5')  # Simulate user input '5' for invalid choice
    # monkeypatch.setattr('builtins.print', lambda _: None)  # Mock print statement to avoid output
    # choice = my_mugwump.attackChoice()
    # assert choice is None  # Invalid choice should return None



def test_attack(my_mugwump):
    # # test attack with claws
    my_mugwump.attackChoice = lambda: 1
    damage = my_mugwump.attack()
    assert damage >= 0
    assert my_mugwump.hitPoints == 20  # Hit points should remain unchanged

    # test attack with fangs
    my_mugwump.attackChoice = lambda: 2
    damage = my_mugwump.attack()
    assert damage >= 0
    assert my_mugwump.hitPoints == 20  # Hit points should remain unchanged

    # test heal
    injuredMugwump = Mugwump(1)
    # artificially set max hitpoints
    injuredMugwump.maxHitPoints = 35
    #injury Mugwump to allow for heal
    injuredMugwump.hitPoints = 20
    my_mugwump.attackChoice = lambda: 3
    damage = my_mugwump.attack()
    assert damage < 0
    # apply heal
    injuredMugwump.takeDamage(damage)
    assert injuredMugwump.hitPoints > 20  # Hit points should remain unchanged

def test_ai(my_mugwump):
    # Test attack_type 1 (Razor-Sharp Claws)
    # Make the d20 roll to return 12 (<=12)
    my_mugwump.d20.roll = lambda: 12
    assert my_mugwump._Mugwump__ai() == 1

    # Test attack_type 2 (Their Fangs of Death)
    # Make the d20 roll to return 17 (12 < x <= 17)
    my_mugwump.d20.roll = lambda: 17
    assert my_mugwump._Mugwump__ai() == 2

    # Test attack_type 3 (Heal)
    # Make the d20 roll to return 18 (>17)
    my_mugwump.d20.roll = lambda: 18
    assert my_mugwump._Mugwump__ai() == 3

    # Test attack_type 2 when d20 roll is 13
    # Make the d20 roll to return 13 (equal to 13)
    my_mugwump.d20.roll = lambda: 13
    assert my_mugwump._Mugwump__ai() == 2


