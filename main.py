import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

off = False

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: {resources['money']}$")

def resource_check():
    if resources['water']>=i1["water"] and resources["milk"]>=i1["milk"] and resources["coffee"]>=i1["coffee"]:
        return True
    else:
        return False

def paise():
    money = 0
    quarters = float(input("How many quarters?: "))
    money += quarters*0.5
    dimes = float(input("How many dimes?: "))
    money += dimes*0.10
    nickels = float(input("How many nickels?: "))
    money += nickels*0.5
    pennies = float(input("How many pennies?: "))
    money += pennies*0.01
    return money

def transaction():
    if p>=cost:
        return True
    else:
        return False

while not off:
    prompts = ["espresso", "latte", "cappuccino", "off", "report"]
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    while not prompt in prompts:
        print("Invalid Input! Try Again!")
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "report":
        report()
        continue
    elif prompt == "off":
        print("Thanx for using our coffee machine\nShutting down...")
        off = True
        break
    else:
        c1 = MENU[prompt]
        cost = c1["cost"]
        r1 = MENU[prompt]
        i1 = r1["ingredients"]

    if not resource_check():
        print("Sorry, There are not enough resources!")
        break
    elif resource_check():
        p = paise()
        if not transaction():
            print("“Sorry that's not enough money. Money refunded.")
            u1s = ["y", "n"]
            u1 = input("Do you wanna try buy again? Type 'y' for yes or 'n' for no: ")
            while not u1 not in u1s:
                print("Invalid Input! Try Again...")
                u1 = input("Do you wanna try buy again? Type 'y' for yes or 'n' for no: ")
            if u1=="y":
                os.system('cls')
                continue
            else:
                print("Thanx for using our machine!")
                break
        if transaction():
            if p>cost:
                xtra = round(p - cost, 2)
                print(f"Here is your ${xtra} in change.")
            resources["money"] += cost
            resources["water"] -= i1["water"]
            resources["milk"] -= i1["milk"]
            resources["coffee"] -= i1["coffee"]
            print(f"Here is your {prompt} ☕ Enjoy!")