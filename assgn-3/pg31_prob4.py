#WAP to print index at which a particular value exists. If multiple values, print all the indices and count the number of time that value is repeated in the list.

list = [3, 2, 1, 2, 4, 5, 2]
value = 2  
indices = []
count = 0

for i, num in enumerate(list):
    if num == value:
        indices.append(i)
        count += 1

print(f"The value {value} appears {count} times in the list.")
print(f"The indices where {value} appears are: {indices}")
