"""This is the Relational Operator from EX01 where the goal is to allow the user to input two numbers and display a series of relations betweent he two numbers."""

left_handed_side: int = int(input("What would you like your Left-handed side value to be? "))
right_handed_side: int = int(input("Now, the Right-handed side value? "))
less_than: int = left_handed_side < right_handed_side
at_least: int = left_handed_side >= right_handed_side
equal_to: int = left_handed_side == right_handed_side
not_equal_to: int = left_handed_side != right_handed_side
print("Left-hand side: " + str(left_handed_side))
print("Right-hand side: " + str(right_handed_side))
print(str(left_handed_side) + " < " + str(right_handed_side) + " is " + str(less_than))
print(str(left_handed_side) + " >= " + str(right_handed_side) + " is " + str(at_least))
print(str(left_handed_side) + " == " + str(right_handed_side) + " is " + str(equal_to))
print(str(left_handed_side) + " != " + str(right_handed_side) + " is " + str(not_equal_to))

__author__ = "730397680"

"""With the relational operator project I first defined the two input variables as integers and than reassigned
the boolean expressions with new variables that would give me my either True or Fase response. From there I just 
produced all the print statements that would show the result of the numbers entered by the user."""
