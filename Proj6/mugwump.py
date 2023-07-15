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

# Create a RealMugwump from the abstract class
class Mugwump(Character):
    def __init__(self, player_pos: int):
        super().__init__(player_pos)
        self.player_pos = player_pos
        self.name = "Mugwump"
        self.user_name= "blank"
        
        # hitpoints, max is set
        # Mugwump uses six d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    # ask user for attack to use
    def attackChoice(self) -> int:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
        # this may need to change, probably needs to move into mugwump and warrior
        # check for applicable attack styles
        while True:
            choices = [1, 2, 3]
            choice = int(input("How would you like to attack?\n"
                               "1. Your claws\n"
                               "2. Your fangs\n"
                               "3. Lick wounds\n"
                               "Enter choice: "))
            if choice in choices:
                return choice
            else:
                print("enter a valid choice")

    # Attack function to determine damage done.  Checks to see if the instance is player or computer controlled
    def attack(self) -> int:

        damage = 0
        # If player, choose attack
        if self.player_pos == 1:
            attack_type = self.attackChoice()
        # If AI, us AI for attack
        else:
            attack_type = self.__ai()
        # Choose attack style
        if (attack_type == 1):
            if (self.d20.roll() >= 13):  # do we hit?
                damage = self.d6.roll() + self.d6.roll()  # 2d6
                print(f"Mugwump hits with claws for {damage}")
            else:
                print(f"Mugwump misses with claws")

        elif (attack_type == 2):
            if (self.d20.roll() >= 16):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"Mugwump hits with fangs for {damage}")
            else:
                print(f"Mugwump misses with fangs")
        else:
            damage = -1 * self.d6.roll()
            print(f"Mugwump heals for {-1*damage}")
        # return the damage
        return damage

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    # Resolve damage
    def takeDamage(self, amount: int): # testable, instructor provided example
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
            # if we actually just healed, we should make sure
            # we don't exceed maxHitpoints
            if (self.hitPoints>self.maxHitPoints):
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0

    def __ai(self) -> int:  # __ means private # testable on range of output
        attack_type = 0
        roll = self.d20.roll()
        # 13 or greater on a d20
        if (roll <= 12):  # 60%
            # Razor-Sharp Claws
            attack_type = 1
        elif (roll <= 17):  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15 %
            attack_type = 3

        return attack_type


