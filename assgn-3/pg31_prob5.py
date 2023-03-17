#WAP that creates a list of words by combining the words in two individual lists.

list1 = ["apple", "banana", "cherry"]
list2 = ["red", "yellow", "green"]

wd_list = []

for wd1 in list1:
    for wd2 in list2:
        cmbd_word = wd1 + " " + wd2
        wd_list.append(cmbd_word)

print(wd_list)
