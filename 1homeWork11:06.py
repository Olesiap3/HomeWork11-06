# Task1 creating two lists
from random import randint
first = list()
second = list()
first.append(sorted([randint(0, 20) for i in range(6)]))
second.append(sorted([randint(0, 20) for i in range(6)]))
print("First List:", first)
print("Second List:", second)

# Task2 creating a third list with elements of two lists
third = first+second
print("Third:", third)

# Task3 creating a third liste without repeating elements
third_1 = sorted(list(set(first) & set(second)))
print(third_1)
