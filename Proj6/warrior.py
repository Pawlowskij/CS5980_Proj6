"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: FIXME
    Created: FIXME
"""
from abc import ABC, abstractmethod
from die import Die
from character import Character



"""
   This method handles the attack logic
   @return the amount of damage an attack has caused, 0 if the attack misses or
           a negative amount of damage if the Mugwump heals itself
 """
# Create a Warrior from the abstract Character class
class Warrior(Character):
    def __init__(self, player_pos: int):
        super().__init__(player_pos)
        self.player_pos = player_pos
        self.name = "Warrior"
        self.user_name = "blank"
        
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
    # ask user for attack to use
    def attackChoice(self) -> int:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
        # check for applicable attack styles
        while True:
            choices = [1, 2]
            choice = int(input("How would you like to attack?\n"
                               "1. Your Trusty Sword\n"
                               "2. Your Shield of Light\n"
                               "Enter choice: "))
            if choice in choices:
                return choice
            else:
                print("enter a valid choice")

    # Attack function to determine damage done.  Checks to see if the instance is player or computer controlled
    def attack(self) -> int:

        damage = 0
        # Checks to see if the instance is player or computer controlled
        if self.player_pos == 1:
            attack_type = self.attackChoice()
        else:
            attack_type = self.__ai()
        # resolve damage based on attack type
        if (attack_type == 1): # trusty sword
            if (self.d20.roll() >= 12):  # do we hit?
                damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                print(f"Warrior hits for {damage}")
            else:
                print("Warrior misses")
        else:  # (attack_type == 2): # shield of light
            if (self.d20.roll() >= 6): # do we hit
                damage = self.d4.roll()  # 1d4 damage
                print(f"Warrior hits for {damage}")
            else:
                print("Warrior misses")
        # return the damage
        return damage


    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """
    # Take damage
    def takeDamage(self, amount: int):
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
        else:
            self.hitPoints = 0

    # AI if player 2 is a warrior, use AI to attack
    def __ai(self) -> int:  # __ means private # testable on range of output
        attack_type = 0
        roll = self.d20.roll()
        # 10 or less on a d20
        if (roll <= 10):  # 50%
            # Sword
            attack_type = 1
        else:  # 50%
            # Shield
            attack_type = 2

        return attack_type
