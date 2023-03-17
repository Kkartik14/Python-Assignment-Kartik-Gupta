#Write the program to find the lists consist of at least one common element. 

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [5, 10, 15, 20]
list4 = [11, 12, 13, 14, 15]
if any(set(list1) & set(other_list) for other_list in [list2, list3, list4]):
    print("At least one common element exists between the lists.")
else:
    print("No common element exists between the lists.")