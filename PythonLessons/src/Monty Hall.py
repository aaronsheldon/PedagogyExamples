import random as rd

def game():
    """
    The classic Monty Hall Game using text inputs. Returns a cross-tabulation of wins and
    loses by choice of swap versus stay:
    * `swapwins` - Number of wins after switching doors.
    * `swaploses` - Number of loses after switching doors.
    * `staywins` - Number of wins after keeping the choice.
    * `staylose` - Number of loses after keeping the choice.
    """

    # The doors as a Python set
    DOORS = { '1', '2', '3' }

    # Cross-tabulations of results
    swapwins = 0
    swaploses = 0
    staywins = 0
    stayloses = 0

    def engine():
        """
        Recursive game engine that runs until exit is chosen.
        """

        # Get access to the cross-tabulations to track between individual games
        nonlocal DOORS
        nonlocal swapwins
        nonlocal swaploses
        nonlocal staywins
        nonlocal stayloses

        # Put a prize randomly behind a door
        prize = rd.choice([ *DOORS ])

        # Prompt the user to choose a door
        first = input("Type '1', '2', or '3' to choose a door.")
        if first not in DOORS:
            return
        
        # Select a door to reveal. Randomly select from the set of doors that neither have
        # the prize nor selected by the user. We can do this by making a set of the prize
        # and the users first choice and removing those from all the doors
        reveal = rd.choice([ *DOORS.difference({ prize, first }) ])

        # Prompt the user to stay or swap with the additional information.
        stay = input(
            f"The prize is not behind door {reveal}." +
            f"Your first choice was door {first}." +
            "Type 'y' to stay with this choice."
        )

        # Update the cross tabulation based on the choices
        if stay == "y" and prize == first:
            staywins += 1
            print("Win!")
        elif stay == "y":
            stayloses += 1
        elif prize == first:
            swaploses += 1
        else:
            swapwins += 1

        # Prompt to continue
        again = input("Type 'y' to play again.")
        if again == "y":
            engine()

    # Initialize the game
    engine()

    # Send the results
    return swapwins, swaploses, staywins, stayloses

print(game())