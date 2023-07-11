from abc import ABC, abstractmethod
from die import Die

# Create abstract class Character

class Character(ABC):
    def __init__(self, player_pos: int): # for homework 4 #, aiController:bool): # testable as well, range of hitpoints, and hitpoints == max hitpoints
        self.player_pos = player_pos
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d8 = Die(8)
        self.d6 = Die(6)
        self.d4 = Die(4)
        self.name = "Character"

        # hitpoints, max is set
        # Mugwump uses six d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    # Abstract Method for Attack
    @abstractmethod
    def attack(self) -> int:
        pass

    # Abstract Method for dealing damage (or healing)
    @abstractmethod
    def takeDamage(self) -> int:
        pass