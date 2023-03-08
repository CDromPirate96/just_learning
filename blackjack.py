############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
import os
def clear_terminal():
    if os.name == "posix":  # for macOS and Linux
        os.system("clear")

from blackjack_art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_Score checking for an 11 (ace). If the score
    # is already over 21, removing the 11 and replacing with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Creating a function called compare() to pass in the user_score and computer_score
# If computer and user both have the same score, then it's a draw.
# If user has a Blackjack (0), then the user wins.
# if user_score is over 21, then user loses.
# If the computer_Score is over 21, then computer loses.
# If none of the above, then the player with the highest score wins.
# If user and computer are both over, you lose.
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # The score will be rechecked with every new card drawn and checks to be repeated until game is end.
    while not is_game_over:
        # Calling calculate_score(). If the computer or the user has a Blackjack (0)
        # or if the user's score is over 21, the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, asking the user if they want to draw another card.
            # if yes, then use the deal_card() function to add another card to user_cards list.
            # If no, then the ga,e had eneded.
            user_should_deal = input("Type 'y' to get anbother card, type 'n' to pass: ")  
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Asking the user if they want to restart the game.
# If they answer yes, clearing the console and starting a new game of Blackjack.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_terminal()
    play_game()
