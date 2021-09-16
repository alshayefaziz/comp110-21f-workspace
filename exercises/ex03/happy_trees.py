"""Drawing forests in a loop."""

__author__ = "730397680"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
trees: str = str(TREE)
depth: int = int(input("Depth: "))
if depth >= 1:
    i: int = 0
    while i < depth:
        print(TREE)
        TREE = TREE + trees
        i = i + 1