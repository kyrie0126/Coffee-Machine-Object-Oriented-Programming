import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initialize objects
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

# things start happening


def coffee_creation():
    drink = str(input(f"Choose from the following drinks '{menu.get_items()}'\n")).lower()

    if drink == "report":
        machine.report()
    elif drink == "off":
        return

    drink_info = menu.find_drink(drink)
    if machine.is_resource_sufficient(drink_info):
        money.make_payment(drink_info.cost)
        machine.make_coffee(drink_info)
        print("\n")
        coffee_creation()
    else:
        return


coffee_creation()





