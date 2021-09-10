"""Repeating a beat in a loop."""

__author__ = "730397680"

counter: int = 1
repeated_beat: str = input("What beat do you want to repeat? ")
amount_of_beats: int = int(input("How many times do you want to repeat it? "))
beat: str = str(repeated_beat)
if amount_of_beats <= counter:
    print("No beat...")
else:
    while counter < amount_of_beats: 
        beat = beat + " " + repeated_beat
        counter = counter + 1
print(beat)

"""I have previous coding experience from my last school so understanding how to assign a string variable
that would allow me to essentially repeat the wanted beat statement was harder. But after sitting on it for a 
little, I come to find out that I was completely overthinking it and could just do the simple addition of string. 
On that thought because we have a while statement along with the use of the counter variable that takes care of the
repetitive fashion that needs to be met."""