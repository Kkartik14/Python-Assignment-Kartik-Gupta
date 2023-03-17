#Write the program to remove the duplicate element of the list.

list = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7]
new_list = list(set(list))

print(new_list)
