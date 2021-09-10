"""Counting letters in a string."""

__author__ = "730397680"


letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
i: int = 0
count: int = 0
while i < len(word):
    if letter == (word[i]):
        count = count + 1
        i = i + 1
    else:
        i = i + 1
print("Count: " + str(count))

"""At first this assignment seemed confusing but after I just assigned the 4 variables and just thought out
my while statement I realised that this was only a 10 line project. The while function was obviously used to start
a loop to allow the program to go through every letter of syntax given by the input of the user. The use of the 
iteration was obviously to eventually work towards the false conclusion of the while statement. What I find most 
interesting out of everything was how I had to put my i = i + 1 in my if condition and else condition which 
kind of threw me for a loop (no pun intended;) )"""