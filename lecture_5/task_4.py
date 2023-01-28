# Задача 4. Да се напише програма, която да пита потребителя да въведе число от
# клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.

# Вход: Enter the number 5
# Изход: Factorial of 5 is 120

number = int(input("Please enter a number > "))


def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)


calc_factorial(number)
print(f"Factorial of {number} is {calc_factorial(number)}")
