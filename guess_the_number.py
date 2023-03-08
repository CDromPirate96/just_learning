import random
random.randint(1, 100)
from guess_the_number_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Tyoe 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeating the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess the number
        guess = int(input("Make a guess: "))

        # Tracking the number of turns and reducing by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()