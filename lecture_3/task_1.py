# Задача 1. Да се напише if-конструкция, която проверява стойността на две целочислени
# променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма от втората.

for i in range(1):
    a = int(input("Please enter a whole number a\n>"))
    b = int(input("Please enter a whole number b\n>"))
    if a > b:
        a_1 = b
        b_1 = a
        print(f"Your numbers are number a={a}, number b={b}")
        print("**********************| Swap values of your numbers |***********************")
        print(f"Number a={a_1}, number b={b_1}")
    else:
        print("Wrong data")
