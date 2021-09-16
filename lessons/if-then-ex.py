"""Practice with if-then-else statements."""

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice >= 25:
        print("B")
    else: 
        print("A")
else: 
    if choice > 75:
        print("C")
    else: 
        print("D")