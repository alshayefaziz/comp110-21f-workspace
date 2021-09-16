"""Finding duplicate letters in a word."""

__author__ = "730397680"


word: str = str(input("Enter a word: "))
dup: bool = False
i: int = 0
while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            dup = True
        j = j + 1
    i = i + 1
print("Found duplicate: " + str(dup))