#WAP to create a list of number in the specified range in particular steps. Reverse the list and prints its values.

start = 1
end = 10
step = 2
my_list = list(range(start, end + 1, step))
reversed_list = my_list[::-1]
print(reversed_list)
