"""
The Die class represents a die with a specified number of sides
(selected by passing an integer to the constructor).
The die must have at least two sides and no more than 100.
If a value outside of this range is attempted, the die should
default to having six sides. The current value of the die
should be set to an integer between one and the number of sides
the die has, chosen at random when the die object is constructed
and whenever the roll() method is called. For example,
for a six sided die, the current value must be set to one of the
 following values with equal likelihood: 1, 2, 3, 4, 5, or 6.

"""
import random
# https://docs.python.org/3/library/random.html
#  random.randint(a, b)
#
#     Return a random integer N such that a <= N <= b.

class Die:

    def __init__(self, numberSides:int): #testable
        # at least two sides and no more than 100, or set to 6
        if (numberSides < 2):
            numberSides = 6
        elif(numberSides > 100):
            numberSides = 6

        self.__numberSides = numberSides # __ means "private"
        #  set a seed that gives predicable
        # random.seed(1)
        self.currentValue = random.randint(1, self.__numberSides)  # set this randomly to start
        # for testing purposes, it may be helpful to try to use a seed, to set your
        # random number generator to return predictable

    # may not need
    # def getCurrentValue(self) -> int:
    #     return self.currentValue

    def roll(self) -> int: # testable
        # update self.numberSides
        self.currentValue = random.randint(1, self.__numberSides)
        return self.currentValue



# test code

# d6 = Die(100) # run random generator
# print(d6.currentValue)
# d6.roll() # run random generator
# print(d6.currentValue)
# print(d6.currentValue)
