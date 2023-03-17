#WAP to create a list of numbers in range 1 to 10. Then delete all the even numbers from the list and print the final list.

list = list(range(1, 11))
for num in list[:]: 
    if num % 2 == 0:
       list.remove(num)
print(list)
