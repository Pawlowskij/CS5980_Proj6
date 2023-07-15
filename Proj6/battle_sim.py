"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: FIXME
    Created: FIXME
"""

from mugwump import Mugwump
from warrior import Warrior
from die import Die
from save_player import save_player
from load_player import *
from bulette import Bulette
from paladin import Paladin

"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. Choose local, and it should find it
"""

"""
     # we need to create a Ten-sided die to be used for checking initiative
"""
d10 = Die(10)


def main():  # not testable
    # Local variables
    # Include any variable that will need to be accessed throughout the program here

    # sentinel value for the game loop
    keep_playing = True

    # String used to determine the winner of the epic battle
    victor = ""
    # game loop

    while keep_playing:
        # print the introduction and rules
        intro()

        # initialize game
        # Initialize the Warrior and Mugwump classes, set the current victor to "none"

        # Have the player select their character

        playerOne = playerOneSelect()
        playerTwo = playerTwoSelect()

        # if you decide to use a Protocol, asset isinstance right here

        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(playerOne, playerTwo)
            victor = battle(playerOne, playerTwo)

            # declare the winner
            if (victor != "none"):  # one of them has won
                report(playerOne, playerTwo)
                victory(victor)
                choice = input("Do you want to save your character?: 'Yes' or 'No'.")
                if choice.lower() == "yes":
                    save_player(playerOne.user_name, playerOne.maxHitPoints, playerOne.hitPoints, playerOne.name)
                # ask to play again
                keep_playing = playAgain()

    # Thank the user for playing your game
    print("Thank you for playing Battle Simulator 3000!")


"""
   This method displays the introduction to the game and gives a description of the rules.
 """


def intro():  # not testable
    # Write a suitable introduction to your game
    print("Welcome to Battle Simulator 3000! The world's more low tech battle simulator!"
          "You are a Valiant Warrior defending your humble village from an evil Mugwump! Fight bravely, "
          "or the citizens of your town will be the Mugwump's dinner!"
          "\nYou have your Trusty Sword, which deals decent damage, but can be tough to hit with sometimes. "
          "You also have your Shield of Light, which is not as strong as your sword, but is easier to deal "
          "damage with."
          "\nLet the epic battle begin!")


# function to select the first character (player controlled)
def playerOneSelect():
    player_file = load_player()
    if player_file != None:
        name, max_hitpoints, current_hp, player_class = player_file

        if player_class == 'Warrior':
            player = Warrior(1)
            player.maxHitPoints = max_hitpoints
            player.hitPoints = current_hp
            player.user_name = name
            return player
        elif player_class == 'Mugwump':
            player = Mugwump(1)
            player.maxHitPoints = max_hitpoints
            player.hitPoints = current_hp
            player.user_name = name
            return player
        elif player_class == 'Bulette':
            player = Bulette(1)
            player.maxHitPoints = max_hitpoints
            player.hitPoints = current_hp
            player.user_name = name
            return player
        elif player_class == 'Paladin':
            player = Paladin(1)
            player.maxHitPoints = max_hitpoints
            player.hitPoints = current_hp
            player.user_name = name
            return player
        else:
            print("Save file is corrupted.")


    else:
        while True:
            player = input("Please select your player: 'Warrior', 'Mugwump', 'Bulette' or Paladin.")
            print(player)
            name = input("What do you want to name your character?")
            if player.lower() == 'warrior':
                player = Warrior(1)
                player.user_name = name
                return player
            elif player.lower() == 'mugwump':
                player = Mugwump(1)
                player.user_name = name
                return player
            elif player.lower() == 'bulette':
                player = Bulette(1)
                player.user_name = name
                return player
            elif player.lower() == 'paladin':
                player = Paladin(1)
                player.user_name = name
                return player
            else:
                print("Please enter either warrior, mugwump, bulette or paladin")


# function to select the computer player
def playerTwoSelect():
    while True:
        player = input("Please select your computer opponent: 'Warrior', 'Mugwump', 'Bulette' or 'Paladin'.")
        if player.lower() == 'warrior':
            return Warrior(2)
        elif player.lower() == 'mugwump':
            return Mugwump(2)
        elif player.lower() == 'bulette':
            return Bulette(2)
        elif player.lower() == 'paladin':
            return Paladin(2)
        else:
            print("Please enter either warrior, mugwump, bulette or paladin")


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
 """


def battle(playerOne, playerTwo):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative()  # this a 1 or 2
    # attack code

    # If the Warrior attacks first
    if (cur_inititive == 1):
        # Warrior attacks and assigns the resulting damage to the mugwump
        print("The first player attacks first!")
        # cur_attack = playerOne.attackChoice()
        damage = playerOne.attack()  # calculate damage caused by warrior
        if damage >= 0:
            playerTwo.takeDamage(damage)  # apply damage to mugwump
        else:
            playerOne.takeDamage(damage)  # heal if player one is a mugwump and heals

        # Check if the Mugwump has been defeated
        if (playerTwo.hitPoints <= 0):
            return "playerOne"
        # If not, Mugwump attacks!
        damage = playerTwo.attack()
        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            playerOne.takeDamage(damage)
        else:  # mugwump healed
            playerTwo.takeDamage(damage)  # healing because it is negative
        if (playerOne.hitPoints == 0):
            return "playerTwo"  # mugwump wins!

    # mugwump attacks first!
    else:
        print("The AI attacks first!")
        # mugwump attacks and assigns the resulting damage to the warrior
        damage = playerTwo.attack()
        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            playerOne.takeDamage(damage)
        else:  # mugwump healed
            playerTwo.takeDamage(damage)  # healing because it is negative

        if (playerOne.hitPoints == 0):
            return "playerTwo"  # mugwump wins!

        # cur_attack = playerOne.attackChoice()
        damage = playerOne.attack()  # calculate damage caused by warrior
        if damage >= 0:
            playerTwo.takeDamage(damage)  # apply damage to mugwump
        else:
            playerOne.takeDamage(damage)  # heal if player one is a mugwump and heals
            print(f"player healed {damage}")
        # Check if the Mugwump has been defeated
        if (playerTwo.hitPoints <= 0):
            return "playerOne"

    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """


def report(playerOne, playerTwo):  # not testable
    print(f"\nPlayerOne HP: {playerOne.hitPoints}")
    print(f"PlayerTwo HP: {playerTwo.hitPoints}")


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the player one goes first, 2 if the computer goes first
 """


# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int:  # return 1 for warrior, 2 for mugwump
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    playerOne_initiative = d10.roll()
    playerTwo_initiative = d10.roll()
    while (playerOne_initiative == playerTwo_initiative):
        playerOne_initiative = d10.roll()
        playerTwo_initiative = d10.roll()

    if (playerOne_initiative > playerTwo_initiative):
        return 1  # Player One goes first
    else:
        return 2  # Player Two goes first


"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """


def victory(victor):  # not testable (or at least we won't worry about testing it)
    if (victor == "playerOne"):
        print("You Win")
    else:
        print("The computer wins.")


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """


def playAgain() -> bool:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    choice = input("Would you like to play again (yes/no)?")
    if (str.lower(choice) == "y" or str.lower(choice) == "yes"):
        return True
    return False


if __name__ == "__main__":
    main()
