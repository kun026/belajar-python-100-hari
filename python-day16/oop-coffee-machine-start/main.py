from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        cash_register.report()
    else:
        order = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(order):
            if cash_register.make_payment(order.cost):
                coffee_machine.make_coffee(order)
