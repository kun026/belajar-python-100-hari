import art
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def check_highest(bidders):
    highest = 0
    winner = ''
    for bidder in bidders:
        bid_price = bidders[bidder]
        if bid_price > highest:
            highest = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")
        
        
auctioneers = {}
        
print(art.logo)
print("Welcome to the secret auction program.")

bidding_finished = False
while not bidding_finished:
    name = input("What is your name? ")
    price = int( input("What's your bid? $"))
    auctioneers[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        clear()
        check_highest(auctioneers)
    elif should_continue == "yes":
        clear()
    else:
        should_continue = input("Please type 'yes' or 'no'\n")
        clear()
        