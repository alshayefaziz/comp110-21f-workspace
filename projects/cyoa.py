"""Choose Your Own Adventure Experience."""

__author__ = "730397680"


SNAKE: str = '\U0001F40D'
TIGER: str = '\U0001F405'
DRAGON: str = '\U0001F409'
player: str
points: int 
monster: str 
moster_name: str


def main() -> None:
    """Programs Entrypoint."""
    global points 
    global monster_name
    points = 0
    fetch_points: int = 0
    feed_points: int = 0
    print(greet())
    monster_name = quiz()
    input("Now that you have decided a name for your monster we can begin your experience as a caretaker!")
    i: int = 0
    while i == 0:
        route: str = str(input(f"Would you like to play fetch, feed or pet {monster_name}? (answer: fetch/feed/pet) "))
        if route == "fetch":
            fetch_points = 0
            fetch_points = fetch(fetch_points)
            points = points + fetch_points
            print(f"You are now currently at {points} care points!")
            i = 0
        else:
            if route == "feed":
                feed_points = 0
                points = feed(feed_points, points)
                print(f"You are now currently at {points} care points!")
                i = 0
            else:
                if route == "pet":
                    i = 1
                else:
                    print("Please make sure that you are entering fetch, feed or pet. Don't forget that it is case sensitive!")
    input(f"Okay {player} you have now completed the game and lets see the results....")
    input(f"{monster_name} your pet {monster},..... *intense drum roll*")
    if points > 0:
        print("Is now taking a nap on your lap, GREAT JOB!:)")
    else:
        if points == 0:
            print("Has run away ;(, which means you ended with 0 points, SO CLOSE! Next time play more fetch!!")
        else:
            if points < 0:
                print("Has BITTEN YOUR HAND OFF :OOOO, NEXT TIME YOU PLAY MAKE SURE YOU PLAY WITH YOUR MONSTER MORE!!!")


def greet() -> None:
    """The player's welcome message."""
    global player
    player = str(input("Woah who goes there? "))
    input(f"Oh {player} we have been expecting you! (press ENT to continue to next line throughout game!)")
    input(f"Well {player}, now that you're here let me explain to you what you will be doing today!")
    input("You will begin with taking a short quiz to determine the kind of monster you will be raising.")
    input("Once your monster is decided you will then name the monster and begin to take care of it and earn care points!")
    input("Here are your care points: 0, ewww.. we don't like to see that, but don't you fret there is an easy way to fix this issue!")
    input("You will earn points by playing fetch with your monster, if the throw is successful you will gain 5 points     however if it is unsuccessful you will only gain 2 points.")
    input("You can then use your care points to feed your monster, grapes cost 2 care points while animal crackers cost 5.")
    input("Throughout the game you will be given the option to pet your monster, this will conclude the game and let you know if you were successful in taking care of your monster.")
    input("If your care points are less than 0 your monster will bite your hand, if your care points are 0 the monster will run away and  if your care points are more than  0 than your monster will take a nap on your lap :)")
    input("Lastly, throughout the game please enter all inputs with correct spelling and all lower case letters, the game is case sensitive!")
    input("Anyways thats enough chitter chatter lets get to caring!")


def quiz() -> str:
    """The player's quiz to see what monster they will be taking care of."""
    input("We will now begin the quiz to assign you your monster!")
    global monster
    global animal
    monster = ""
    animal = ""
    i: int = 0
    while i == 0:
        question_one: str = str(input("Do you want a small or big pet? (answer with small or big) "))
        if question_one == "small":
            question_two: str = str(input("Do you want your pet to get around on legs? (answer: yes or no) "))
            if question_two == "yes":
                monster = "Tiger" + TIGER
                print(f"You are now taking care of a monster {monster}!")
                i = 1
            else:
                if question_two == "no":
                    monster = "Snake" + SNAKE
                    print(f"You are now taking care of a monster {monster}!")
                    i = 1
                else:
                    print("Please make sure that your response is either yes or no and do not forget that it is case sensitve!")
                    i = 0
        else:
            if question_one == "big":
                question_three: str = str(input("Do you want your pet to be able to fly? (answer: yes or no) "))
                if question_three == "yes": 
                    monster = "Dragon" + DRAGON
                    print(f"You are now taking care of a monster {monster}!")
                    i = i + 1
                else:
                    if question_three == "no":
                        monster = "Tiger" + TIGER
                        print(f"You are now taking care of a monster {monster}!")
                        i = i + 1
                    else:
                        print("Please make sure that your response is either yes or no and do not forget that it is case sensitve!")
            else:
                print("Please make sure that your response is either small or big, and do not forget that it is case sensitive!")
    nick_name: str = str(input(f"Now that you have the type of monster decided it is time to name your {monster}! "))
    animal = animal + nick_name
    input(f"Congrats on adopting {animal}!")        
    return animal


def fetch(play: int) -> int:
    """The fetch game that lets the player gain care points!"""
    from random import randint
    input(f"Alright you will now play fetch with {monster_name}!")
    input("The way this works is that you will guess a number 1 through 3...")
    input("If you guess the right number the throw will count as successful and you will gain 5 care points!")
    input("However if you are unsuccessful you will only gain 2 points.")
    input("Now lets get started!")
    i: int = 0
    c: int = 0
    while i == 0:
        while c == 0:
            j: int = 0
            guess: int = int(input("Guess a number 1 through 3. "))
            correct_guess: int = int(randint(1, 3))
            if guess < 1 or guess > 3:
                print("Please make sure that you only guess numbers 1 through 3!")
                c = 0
            else:
                if guess == correct_guess:
                    play = play + 5
                    print(f"You now have {play} care points!")
                    c = 1
                else: 
                    if guess != correct_guess:
                        play = play + 2
                        print(f"You now have {play} care points!")
                        c = 1
        while j == 0:                
            repeat: str = str(input("Would you like to play again? (answer: yes/no) "))
            if repeat == "yes":
                i = 0
                j = 1
                c = 0 
            else:
                if repeat == "no":
                    i = 1
                    j = 1
                else:
                    print("Please make sure that you enter yes or no. Do not forget that it is case sensitive!")
                    j = 0
    return play


def feed(food: int, total: int) -> int:
    """The feed option where players can use care points to feed their monster!"""
    input(f"Alright you will now begin feeding {monster_name}! Grapes cost 2 care points while animal crackers cost 5!")
    input(f"Don't forget that this does cost care points, you currently have {total} so spend them wisely!")
    i: int = 0 
    while i == 0: 
        j: int = 0
        c: int = 0
        while c == 0:
            route: str = str(input(f"Would you like to feed {monster_name} grapes or crackers? (answer: grapes/crackers) "))
            if route == "grapes":
                total = total - 2
                food = food + 2
                c = 1
                print(f"You have now spent a total of {food} care points and have a total of {total} care points.")
            else:
                if route == "crackers":
                    total = total - 5
                    food = food + 5
                    c = 1
                    print(f"You now have a total of {total} care points.")
                else:
                    print("Please make sure that you enter grapes or crackers. Do not forget that it is case sensitive!")
                    c = 0 
        while j == 0:
            repeat: str = str(input(f"Would you like to feed {monster_name} again? (answer: yes/no) "))           
            if repeat == "yes":
                i = 0
                j = 1
                c = 0
            else:
                if repeat == "no":
                    i = 1
                    j = 1
                else: 
                    print("Please make sure that you enter yes or no. Do not forget that it is case sensitive!")
                    j = 0
    return total


if __name__ == "__main__":
    main()