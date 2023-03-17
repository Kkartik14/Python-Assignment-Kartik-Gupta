#WAP that creates a list of numbers from 1-20 that are either divisible by 2 or divisible by 4.

list = []

for i in range(1, 21):
    if i % 2 == 0 or i % 4 == 0:
        list.append(i)

print(list)
