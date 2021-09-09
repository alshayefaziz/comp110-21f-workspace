"""This is the Numeric Operator from EX01 where you should be able to input two numbers and 4 different math functions should be presented correctly to you after your input."""

left_handed_side: int = int(input("What would you like your Left-handed side value to be? "))
right_handed_side: int = int(input("Now, the Right-handed side value? "))
power: int = left_handed_side ** right_handed_side
division: int = left_handed_side / right_handed_side
int_division: int = left_handed_side // right_handed_side
remainder: int = left_handed_side % right_handed_side
print("Left-hand side: " + str(left_handed_side))
print("Right-hand side: " + str(right_handed_side))
print(str(left_handed_side) + " ** " + str(right_handed_side) + " is " + str(power))
print(str(left_handed_side) + " / " + str(right_handed_side) + " is " + str(division))
print(str(left_handed_side) + " // " + str(right_handed_side) + " is " + str(int_division))
print(str(left_handed_side) + " % " + str(right_handed_side) + " is " + str(remainder))

__author__ = "730397680"

"""With the numeric operator program the way I approached it is how we did the LS07 diagram. I start off by assigning
variable names to the initial input values by the user. After making two separate input statements for both of the
numbers I then thought it would be easier to go ahead and assign variable names and assign the computation that
goes along with each variable because I kind of like the organization pattern of all computations followed by
all print statments with this experiment. After each computation was assigned a variable name and a task to complete
with the inputs by the user I then began my print statements which would first display the users input values and 
which one the put in as the left hand side value and which one they put as the right hand side value. After that
there is essentially 4 print statements which look extremely similar but obviously all print out a different operator
and the value computed by use of that operator."""