import pytest
from battle_sim import playerOneSelect, playerTwoSelect, playAgain, initiative
from mugwump import RealMugwump
from warrior import RealWarrior
from die import Die
import random
from unittest.mock import patch

# Check for either warrior or mugwump entry on first player selection
def test_playerOneSelect(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Warrior')
    assert isinstance(playerOneSelect(), RealWarrior)

    monkeypatch.setattr('builtins.input', lambda _: 'Mugwump')
    assert isinstance(playerOneSelect(), RealMugwump)

# Check for either warrior or mugwump entry on second player selection
def test_playerTwoSelect(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Warrior')
    assert isinstance(playerTwoSelect(), RealWarrior)

    monkeypatch.setattr('builtins.input', lambda _: 'Mugwump')
    assert isinstance(playerTwoSelect(), RealMugwump)

# Create fixture for Dice D10
@pytest.fixture
def d10():
    # Set the seed to control randomness
    random.seed(42)
    return Die(10)

# Roll dice and check for results to be either 1 or 2
def test_initiative(d10):
    result = initiative()
    assert result in [1, 2]

def test_playAgain(monkeypatch):
    # Simulate user input 'yes'
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    assert playAgain() is True

    # Simulate user input 'no'
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    assert playAgain() is False

    # Simulate invalid user input
    monkeypatch.setattr('builtins.input', lambda _: 'invalid')
    assert playAgain() is False
