# Disclaimer: gubot pa kaayu, ako lang ihatag daan para maka sugod nata ug construct sa code.

import random
import time

print("-------------------------------")
print("-- Welcome to the MorseZone! --")
print("-------------------------------\n")


# Define Morse code patterns and their corresponding letters
morse_codes = {".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e',
               "..-.": 'f', "--.": 'g', "....": 'h',
               "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l', "--": 'm',
               "-.": 'n', "---": 'o', ".--.": 'p',
               "--.-": 'q', ".-.": 'r', "...": 's', "-": 't', "..-": 'u',
               "...-": 'v', ".--": 'w', "-..-": 'x',
               "-.--": 'y', "--..": 'z'}



# Handle gamemode choice
def gameMode():

    choice = int(input("choose a game mode Normal (1) or Timed (2): "))

    if choice == 1:
        normal()
    elif choice == 2:
        timed()
    else:
        print(f"Invalid choice\n")

    return" "

# handle rerun
def rerun():  # Handle rerun function

    choice1 = input("\nWould you like to play again Y|N?\n").upper()

    if choice1 == "Y":
        print(gameMode())
    elif choice1 == "N":
        print("\nOkay! see you next time!")
    else:
        print("That is invalid!")
        rerun()


# handle normal game mode with 5 questions
def normal():
    score = 0
    for x in range(5):
        # Randomly select a Morse code pattern
        random_morse = random.choice(list(morse_codes.keys()))

        # Print a message to the user
        print("\nGuess the letter for the following Morse code:")
        print(random_morse)

        # Get user input
        user_input = input(">> ").lower()

        # Check if the user's input matches the correct answer
        correct_answer = morse_codes[random_morse]

        if user_input == correct_answer:
            score += 1
            print("⭐ Nice! You guessed it correctly! ⭐")

        else:
            print(f"Wrong. The correct answer is '{correct_answer}'.")

    print(f"your score is: {score}")

    rerun()

    return " "



# handle timed gamemode with timer
def timed():
    # Initialize Score
    score = 0

    # Setting the time limit
    game_duration = 60  # 1 minute playing time

    # Formula
    start_time = time.time()
    end_time = start_time + game_duration

    while time.time() < end_time:
        # Calculates time
        remaining_time = int(end_time - time.time())

        # Randomly select a Morse code pattern
        random_morse = random.choice(list(morse_codes.keys()))

        # Print a message to the user
        print("\nRemaining time: {} seconds".format(remaining_time))
        print("Guess the letter for the following Morse code:")
        print("\t", random_morse)

        # Get user input
        user_input = input(">> ").lower()

        # Check if the user's input matches the correct answer
        correct_answer = morse_codes[random_morse]

        if user_input == correct_answer:
            print("⭐ Nice! You guessed it correctly! ⭐")
            score += 1
        else:
            print(f"Wrong. The correct answer is '{correct_answer}'.")

    # Displaying the score
    print(f"Time's up! Your total score is {score}.")

    rerun()

    return" "


gameMode()
