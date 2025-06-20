from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

is_on = True



while is_on:
    option = menu.get_items()
    choice = input(f"What would you like {option}:").lower()

    if is_on == "off":
        is_on = False

    elif choice == "report":
        coffee.report()
        money.report()

    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)



