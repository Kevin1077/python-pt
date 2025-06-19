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
cont = True
def option(menu1):

    quarter = int(input("Please insert coins.\nhow many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    cash_available = quarter * 0.25 + dime * 0.10 + nickles * 0.05 + pennies * 0.01
    check(cash_available, menu1)


def check(cash_available, menu):
      if menu["choice"]["cost"] < cash_available:
        print("Sorry that's not enough money. Money refunded.")


      else:
        change = cash_available - menu["choice"]["cost"]
        print(f"Here is {change} in change.\nHere is your espresso ☕️. Enjoy!")
        global profit
        profit += menu["choice"]["cost"]

def backup(choice1, menu3):
    for item in choice1["ingredients"]:
        resources[item] -= choice1[item]




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
        option(MENU)
        backup(choice, MENU)

