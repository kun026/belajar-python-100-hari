MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(ingredients):
    """
    Checks if the required resources for making a drink are available.

    Parameters:
        ingredients (dict): A dictionary containing the required ingredients for a specific drink.

    Returns:
        bool: True if all resources are available, False if any resource is insufficient.
    """
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True

def process_coins():
    """
    Processes the coins inserted by the user for purchasing a drink.

    Returns:
        float: Total value of the coins inserted in dollars.
    """
    quarters = int( input("How many quarters?: ")) * 0.25
    dimes = int( input("How many dimes?: ")) * 0.1
    nickles = int( input("How many nickles?: ")) * 0.05
    pennies = int( input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_recived, drink_cost):
    """
    Checks if the purchase transaction is successful.

    Parameters:
        money_received (float): Total money received from the user.
        drink_cost (float): The cost of the drink being purchased.

    Returns:
        bool: True if the transaction is successful, False otherwise.
    """
    if money_recived >= drink_cost:
        change = round(money_recived  - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, ingredients):
    """
    Makes a coffee drink using the provided ingredients.

    Parameters:
        drink_name (str): The name of the drink to be made.
        ingredients (dict): A dictionary containing the required ingredients for the drink.
    """
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])