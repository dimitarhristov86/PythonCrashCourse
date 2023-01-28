# Задача 1. Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.

# Вход: [1, 2, 5, 9, 10], 5
# Изход: Position 2

# Вход: [1, 2, 5, 9, 10], 3
# Изход: Not found


numbers = [1, 2, 5, 9, 10]


def find_number_index(nums):
    number = int(input('Please enter a whole number between 1 and 10 to check its index\n>'))
    if number in nums:
        number_index = numbers.index(number)
        print(f"Position {number_index}")
    else:
        print("Not found")


find_number_index(numbers)
