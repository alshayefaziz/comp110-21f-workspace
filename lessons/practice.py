counter: int = 1
repeated_beat: str = input("What beat do you want to repeat? ")
amount_of_beats: int = int(input("How many times do you want to repeat it? "))
beat: str = str(repeated_beat)
if amount_of_beats > counter:
    while amount_of_beats > counter:
        beat = beat + " " + repeated_beat
        counter = counter + 1
    print(beat)
else:
    print("No beat...")