import pytest

from bulette import Bulette
from die import Die

# create fixture bulette
@pytest.fixture
def my_bulette():
    bulette = Bulette(1)
    d10 = Die(10)

    # artificially set max hitpoints
    bulette.maxHitPoints = 60
    bulette.hitPoints = 60
    return bulette

# test that mugwump HP is same as the Max HP at initialization
def test_Mugwump_hitpoints():
    # Create a Mugwump object
    buletteHP = Bulette(1)
    assert buletteHP.maxHitPoints == buletteHP.hitPoints
    # Test that HP is between 6 and 60
    assert 6 <= buletteHP.maxHitPoints <= 60


def test_take_damage(my_bulette):
    # check for damage of 5 resulting in 15
    my_bulette.takeDamage(5)
    assert (my_bulette.hitPoints == 55)

    # overheal should return max HP
    my_bulette.takeDamage(-100)
    assert (my_bulette.hitPoints == 60)

    # overkill should return 0 HP
    my_bulette.takeDamage(2000000)
    assert (my_bulette.hitPoints == 0)

    # Test valid attack choice
def test_attackChoice(monkeypatch, my_bulette):
    # Simulate user input '1' for claws attack
    monkeypatch.setattr('builtins.input', lambda _: '1')
    choice = my_bulette.attackChoice()
    assert choice == 1

    # Simulate user input '2' for fangs attack
    monkeypatch.setattr('builtins.input', lambda _: '2')
    choice = my_bulette.attackChoice()
    assert choice == 2

    # Simulate user input '3' for heals attack
    monkeypatch.setattr('builtins.input', lambda _: '3')
    choice = my_bulette.attackChoice()
    assert choice == 3

    # # Test invalid attack choice -- creates an infinite loop because of While True in attackChoice??
    # monkeypatch.setattr('builtins.input', lambda _: '5')  # Simulate user input '5' for invalid choice
    # monkeypatch.setattr('builtins.print', lambda _: None)  # Mock print statement to avoid output
    # choice = my_mugwump.attackChoice()
    # assert choice is None  # Invalid choice should return None



def test_attack(my_bulette):
    # # test attack with claws
    my_bulette.attackChoice = lambda: 1
    damage = my_bulette.attack()
    assert damage >= 0
    assert my_bulette.hitPoints == 60  # Hit points should remain unchanged

    # test attack with fangs
    my_bulette.attackChoice = lambda: 2
    damage = my_bulette.attack()
    assert damage >= 0
    assert my_bulette.hitPoints == 60  # Hit points should remain unchanged

    # test heal
    injuredBulette = Bulette(1)
    # artificially set max hitpoints
    injuredBulette.maxHitPoints = 55
    #injury Mugwump to allow for heal
    injuredBulette.hitPoints = 60
    my_bulette.attackChoice = lambda: 3
    damage = my_bulette.attack()
    assert damage < 0
    # apply heal
    injuredBulette.takeDamage(damage)
    assert injuredBulette.hitPoints > 20  # Hit points should remain unchanged

def test_ai(my_bulette):
    # Test attack_type 1 (Razor-Sharp Claws)
    # Make the d20 roll to return 12 (<=12)
    my_bulette.d20.roll = lambda: 12
    assert my_bulette._Bulette__ai() == 1

    # Test attack_type 2 (Their Fangs of Death)
    # Make the d20 roll to return 17 (12 < x <= 17)
    my_bulette.d20.roll = lambda: 17
    assert my_bulette._Bulette__ai() == 2

    # Test attack_type 3 (Heal)
    # Make the d20 roll to return 18 (>17)
    my_bulette.d20.roll = lambda: 18
    assert my_bulette._Bulette__ai() == 3

    # Test attack_type 2 when d20 roll is 13
    # Make the d20 roll to return 13 (equal to 13)
    my_bulette.d20.roll = lambda: 13
    assert my_bulette._Bulette__ai() == 2


