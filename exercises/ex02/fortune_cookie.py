"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730397680"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


fortune_saying: int = int(randint(1, 4))
fortune_1: str = ("Tomorrow will be the start of a powerful new journey!")
fortune_2: str = ("True love is right in front of you, you just have to open your eyes.")
fortune_3: str = ("You must love yourself before you are able to love others!")
fortune_4: str = ("You already know what the next step required is, you just have to take it!")
print("Your fortune cookie says...")
if fortune_saying == 1:
    print(fortune_1)
else:
    if fortune_saying == 2:
        print(fortune_2)
    else:
        if fortune_saying == 3:
            print(fortune_3)
        else:
            print(fortune_4)
print("Now, go spread positive vibes!")

"""At first the point of the "from random import randint" function really confused me but after messing with it
for a while I understood how I could assign the randomly assigned number prdouced from a set value to my 
fortune_saying variable as an integer which then allowed me to immediately follow up with a nested if/else 
conditional statement which was pretty easy to setup."""