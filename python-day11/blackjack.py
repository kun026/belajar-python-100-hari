from art import logo
import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Calculate the total value of cards in a blackjack game.
    
    Args:
    cards (list): A list containing the values of each card in the blackjack game.
    
    Returns:
    int: The total value of the cards in the blackjack game.
    
    Explanation:
    This function takes a list containing the values of cards in a blackjack game
    and returns the total value of those cards. If the total card value is 21
    and the number of cards is 2, the function returns 0 (natural blackjack).
    If there is an Ace card with a value of 11 and the total card value exceeds
    21, the value of the Ace card will be changed to 1. After that, the function
    returns the total value of the cards.
    """
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    else:
        return score

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, Opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over, You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    print(logo)

    user_cards = []
    comp_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:    
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
                
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)
        
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))
    
while input("Do You want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
    