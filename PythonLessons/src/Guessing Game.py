# External libraries for Regular Expressions and Random numbers
import re, random

def guessinggame():
    """
    Prompt the terminal user to guess a number. Provide hints as to whether the guess is
    too small, or too large.
    """
    SECRET = random.randint(1, 10)
    MATCH = re.compile("^-?[1-9]+[0-9]*$")

    # We need some code to end the program if they type 'q'
    name = input("What is your name, type 'q' to quit?\n")
    if name == "q":
        print("Goodbye.")
        return
    
    # Ask if they want to play
    choice = input(
        f"Hello {name} do you want to play a number guessing game, " +
        "type 'y' for yes and 'n' for no?\n"
    )

    # Keep prompting until a yes or no answer
    while choice not in ["n", "y"]:
        choice = input(
            f"I am sorry {name} I did not understand your choice, " +
            "type 'y' for yes and 'n' for no.\n"
        )

    # They do not want to play
    if choice == "n":
        print(f"Goodbye {name}.")
        return
    
    # Initial guess
    guess =  input("Please guess a number between 1 and 10, type 'q' to quit.\n")

    # Main game loop, Prompt whether bigger or smaller
    while True:
        if guess == "q":
            print(f"Goodbye {name}.")
            return
        
        # Check for a string that contains a number
        if not MATCH.match(guess):
            guess = input(
                "I did not understand the input. Please guess again. " +
                "Type 'q' to quit.\n"
            )
            continue

        # We can safely convert guess to an integer because we made it passed the
        # continue in the conditional that checks for an integer
        guess = int(guess)
        if guess < SECRET:
            guess = input("Too small. Try again. Type 'q' to quit.\n")
            continue
        if guess > SECRET:
            guess = input("Too big. Try again. Type 'q' to quit.\n")
            continue

        # The loop breaks only if the guess is correct
        break

    # End of game
    print(f"Congratulations {name} you guessed correctly!")

# Test the game
guessinggame()