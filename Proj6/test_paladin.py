import pytest

from paladin import Paladin
from die import Die

# create fixture Paladin
@pytest.fixture
def my_paladin():
    paladin = Paladin(1)
    d10 = Die(10)

    # artificially set max hitpoints
    paladin.maxHitPoints = 60
    paladin.hitPoints = 60
    paladin.attack_buff = 1
    return paladin

# test that Paladin HP is same as the Max HP at initialization
def test_Paladin_hitpoints():
    # Create a Paladin object
    paladinHP = Paladin(1)
    assert paladinHP.maxHitPoints == paladinHP.hitPoints
    # Test that HP is between 6 and 60
    assert 6 <= paladinHP.maxHitPoints <= 60


def test_take_damage(my_paladin):
    # check for damage of 5 resulting in 15
    my_paladin.takeDamage(5)
    assert (my_paladin.hitPoints == 55)

    # overheal should return max HP
    my_paladin.takeDamage(-100)
    assert (my_paladin.hitPoints == 60)

    # overkill should return 0 HP
    my_paladin.takeDamage(2000000)
    assert (my_paladin.hitPoints == 0)

    # Test valid attack choice
def test_attackChoice(monkeypatch, my_paladin):
    # Simulate user input '1'
    monkeypatch.setattr('builtins.input', lambda _: '1')
    choice = my_paladin.attackChoice()
    assert choice == 1

    # Simulate user input '2'
    monkeypatch.setattr('builtins.input', lambda _: '2')
    choice = my_paladin.attackChoice()
    assert choice == 2

    # Simulate user input '3' for buff
    monkeypatch.setattr('builtins.input', lambda _: '3')
    choice = my_paladin.attackChoice()
    assert choice == 3

    # Simulate user input '4' for heal
    monkeypatch.setattr('builtins.input', lambda _: '4')
    choice = my_paladin.attackChoice()
    assert choice == 4

    # # Test invalid attack choice -- creates an infinite loop because of While True in attackChoice??
    # monkeypatch.setattr('builtins.input', lambda _: '5')  # Simulate user input '5' for invalid choice
    # monkeypatch.setattr('builtins.print', lambda _: None)  # Mock print statement to avoid output
    # choice = my_paladin.attackChoice()
    # assert choice is None  # Invalid choice should return None



def test_attack(my_paladin):
    # # test attack with Mac
    my_paladin.attackChoice = lambda: 1
    damage = my_paladin.attack()
    assert damage >= 0
    # Hit points should remain unchanged
    assert my_paladin.hitPoints == 60

    # test attack with Shield
    my_paladin.attackChoice = lambda: 2
    damage = my_paladin.attack()
    assert damage >= 0
    # Hit points should remain unchanged
    assert my_paladin.hitPoints == 60

    # test attack with Buff
    my_paladin.attackChoice = lambda: 3
    damage = my_paladin.attack()
    my_paladin.attack_buff += 0.1
    assert my_paladin.attack_buff == 1.1

    # test heal
    # create Paladin instance to injure
    injuredPaladin = Paladin(1)

    # artificially set max hitpoints
    injuredPaladin.maxHitPoints = 55

    # injure Paladin to allow for heal
    injuredPaladin.hitPoints = 60
    my_paladin.attackChoice = lambda: 4
    damage = my_paladin.attack()
    assert damage < 0

    # apply heal
    injuredPaladin.takeDamage(damage)
    assert injuredPaladin.hitPoints > 20  # Hit points should remain unchanged

def test_ai(my_paladin):
    # Test attack_type 1
    # Make the d20 roll to return 5
    my_paladin.d20.roll = lambda: 5
    assert my_paladin._Paladin__ai() == 1

    # Test attack_type 2
    # Make the d20 roll to return 10
    my_paladin.d20.roll = lambda: 10
    assert my_paladin._Paladin__ai() == 2

    # Test attack_type 3 (Buff)
    # Make the d20 roll to return 15
    my_paladin.d20.roll = lambda: 15
    assert my_paladin._Paladin__ai() == 3

    # Test attack_type 2 when d20 roll is 13
    # Make the d20 roll to return 13 (equal to 13)
    my_paladin.d20.roll = lambda: 18
    assert my_paladin._Paladin__ai() == 4


