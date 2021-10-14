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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


# print(MENU["espresso"]["ingredients"]["water"])


def print_report(m):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${m}")




def check_ingredient(ch):
    if ch == "e":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                return "ok"
            else:
                return "coffee"
        else:
            return "water"
    elif ch == "l":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    return "ok"
                else:
                    return "coffee"
            else:
                return "milk"
        else:
            return "water"
    elif ch == "c":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    return "ok"
                else:
                    return "coffee"
            else:
                return "milk"
        else:
            return "water"


def ask_money():
    collect_m = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    print("Please insert coins")
    collect_m["quarters"] = int(input("How many quarters?: "))
    collect_m["dimes"] = int(input("How many dimes?: "))
    collect_m["nickles"] = int(input("How many nickles?: "))
    collect_m["pennies"] = int(input("How many pennies?: "))

    return collect_m["quarters"] * 0.25 + collect_m["dimes"] * .10 + collect_m["nickles"] * 0.05 + collect_m[
        "pennies"] * 0.01


def reduce_inventory(redCh):
    if redCh == "e":
        print("reduce e")
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif redCh == "l":
        print("reduce l")
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    elif redCh == "c":
        print("reduce c")
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]


flag = True
while flag:
    user_ch = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_ch == "report":
        print_report(money)
    elif user_ch == "espresso":
        print("e")
        if check_ingredient("e") == "ok":
            am = ask_money()
            if am < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f"Here is $" + "{:.2f}".format(am - MENU['espresso']['cost']) + " in change.")
                print(f"Here is your {user_ch} ☕. Enjoy!")
                money += MENU['espresso']['cost']
                reduce_inventory("e")
        else:
            print(f"Sorry there is not enough {check_ingredient('e')}")
    elif user_ch == "latte":
        print("l")
        if check_ingredient("l") == "ok":
            am = ask_money()
            print(am)
            if am < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f"Here is $" + "{:.2f}".format(am - MENU['latte']['cost']) + " in change.")
                print(f"Here is your {user_ch} ☕. Enjoy!")
                money += MENU['latte']['cost']
                reduce_inventory("l")
        else:
            print(f"Sorry there is not enough {check_ingredient('l')}")
    elif user_ch == "cappuccino":
        print("c")
        if check_ingredient("c") == "ok":
            am = ask_money()
            if am < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f"Here is $" + "{:.2f}".format(am - MENU['cappuccino']['cost']) + " in change.")
                print(f"Here is your {user_ch} ☕. Enjoy!")
                money += MENU['cappuccino']['cost']
                reduce_inventory("c")
        else:
            print(f"Sorry there is not enough {check_ingredient('c')}")
    elif user_ch == "off":
        flag = False
    else:
        print("Wrong Choice")

# TODO 1. Print welcome
# TODO 2. Report
# TODO 3. Input from user
# TODO 4. Ask for money
# TODO 5. Check enough money, if not quit
# TODO 6. Check inventory on user choice
