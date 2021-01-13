print("Welcome to the treasure island, your mission is to find the treause")
start= int(input("Press 1 to start the game or 2 to quit\n"))

while start==1:
    start=input("Do you want to go left or right?\n").lower()
    if start=="left":
        two=input("Do you want to swim or wait\n").lower()
        if two=="wait":
            three=input("which door do you want to take? Red, Blue or Yellow\n").lower()
            if three=="yellow":
                print("you win")
                start = int(input("Press 1 to start the game or 2 to quit\n"))
            else:
                print("You loose")
                start = int(input("Press 1 to start the game or 2 to quit\n"))
        else:
            print("game over")
            start = int(input("Press 1 to start the game or 2 to quit\n"))

    else:
        print("Game over")
        start = int(input("Press 1 to start the game or 2 to quit\n"))