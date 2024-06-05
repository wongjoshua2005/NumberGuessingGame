import random # Needed for the random number generator

print("Joshua Wong's Number Guessing Game!\n")

# Uses loop to ensure the game can still be replayed again
while True:
    # To show the user's choices for difficulty
    print("Difficulty List:")
    print("1. Easy (0 - 9)\n2. Medium (10 - 49)\n3. Hard (50 - 99)\n" +
    "4. Extreme (100 - 1000)\n")

    # To ask the user for selecting a difficulty choice.
    askDifficulty = int(input("Select a difficulty by choosing a number! "))

    # Variables for number of tries user have currently and the random number
    num = 0
    numOfTries = 0

    # Randomly generates a number based on difficulty level
    match askDifficulty:
        case 1:
            num = random.randint(0, 9)
        case 2:
            num = random.randint(10, 49)
        case 3:
            num = random.randint(50, 99)
        case 4:
            num = random.randint(100, 1000)
        case _:
            print("Invalid difficulty choice.")
            continue
    
    print("You have six tries! Good luck! :)")

    # For the user to guess a number under the limit
    while numOfTries < 6:
        answer = int(input("Enter your answer "))

        # Immediately quits when player guesses correctly
        if answer == num:
            print("Congrats you won the game!")
            exit()

        numOfTries += 1

    print("Sorry. It looks like you lost the game. Try again?")
    retry = input("Enter either Y or N: ") # Gives the user ability to retry

    # Checks choices if the user wants to quit the game or not
    match retry:
        case "Y":
            continue
        case "N":
            exit()
        case _:
            print("Automatically assumes any other choice means to exit.")
            exit()