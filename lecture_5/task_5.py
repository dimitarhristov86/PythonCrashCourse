# Задача 5. Да се създаде програма, която да реализира няколко функции: добавяне (Add),
# изтриване (Remove), изтриване на всичко (clear), показване (show), край на програмата
# (Quit). Програмата да реализира програмна логика за количка за пазаруване (като тези
# в онлайн магазините). Потребителят да въвежда от клавиатурата даден елемент, след
# което да има възможност да го добави, изтрие, да види какво е поръчал.

print("Welcome to Python Crash Course Beginners Shop! ")
print("--------------------------------")
item = input("Please enter a product > ")
print(f"You've entered a '{item}'")
print("--------------------------")
basket = []
after_actions = {"R": "Remove product from basket",
                 "C": "Clear basket",
                 "S": "Show basket",
                 "Q": "Quit"}

actions = {"A": "Add product to basket",
           "R": "Remove product from basket",
           "C": "Clear basket",
           "S": "Show basket",
           "Q": "Quit"}

print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
action = input(f"Chose an action:\n> ").lower()


def add_product():
    basket.append(item)
    print(f"You added '{item}' to you basket ")


def remove_product():
    print("Your basket:", *basket, sep="\n")
    removed_item = input("Which product do you want to remove?\n> ")
    if removed_item in basket:
        basket.remove(removed_item)
        print(f"You removed '{removed_item}' from your basket ")
    elif removed_item not in basket:
        print("Selected product is not in your basket!")


def clear_basket():
    basket.clear()
    print("Your basket has been cleared! ")
    print("Your basket:", *basket, sep="\n")


def show_basket():
    print("-------------------------------")
    print("Your basket:", *basket, sep="\n")
    print("-------------------------------")


while action not in actions.keys():
    if action == "a":
        add_product()
        show_basket()
        new_action = input("Do you want to continue shopping? Y(Yes), N(No) ").lower()
        if new_action == "y":
            item = input("Please enter a product > ")
            print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
            action = input(f"Chose an action:\n> ").lower()
        if new_action == "n":
            show_basket()
            print('\n'.join(f'{key}: {value}' for key, value in after_actions.items()))
            action = input(f"Chose an action:\n> ").lower()
    elif action == "r":
        remove_product()
        show_basket()
        new_action = input("Do you want to continue shopping? Y(Yes), N(No) ").lower()
        if new_action == "y":
            item = input("Please enter a product > ")
            print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
            action = input(f"Chose an action:\n> ").lower()
        if new_action == "n":
            show_basket()
            print('\n'.join(f'{key}: {value}' for key, value in after_actions.items()))
            action = input(f"Chose an action:\n> ").lower()
    elif action == "c":
        clear_basket()
        new_action = input("Do you want to continue shopping? Y(Yes), N(No) ").lower()
        if new_action == "y":
            item = input("Please enter a product > ")
            print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
            action = input(f"Chose an action:\n> ").lower()
        if new_action == "n":
            show_basket()
            print("Thank you for shopping with us! ")
            quit()
    elif action == "s":
        show_basket()
        new_action = input("Do you want to continue shopping? Y(Yes), N(No) ").lower()
        if new_action == "y":
            item = input("Please enter a product > ")
            print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
            action = input(f"Chose an action:\n> ").lower()
        if new_action == "n":
            show_basket()
            print('\n'.join(f'{key}: {value}' for key, value in after_actions.items()))
            action = input(f"Chose an action:\n> ").lower()
    elif action == "q":
        print("Thank you for shopping with us! ")
        quit()
    elif action not in actions:
        print("Unrecognized action, please try again! ")
        print('\n'.join(f'{key}: {value}' for key, value in actions.items()))
        action = input(f"Chose an action:\n> ").lower()


