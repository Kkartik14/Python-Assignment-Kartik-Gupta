#WAP that creates a list of 10 random integers. Then creates two lists--- Odd list and Even list that has all odd and even values in the list respectively. 

import random

my_list = [random.randint(1, 100) for _ in range(10)]
odd_list = []
even_list = []
for num in my_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Original list:", my_list)
print("Odd list:", odd_list)
print("Even list:", even_list)
