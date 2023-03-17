#WAP to generate in the Fibonacci sequence and store it in the list. Then find the sum of the even-valued terms.

num_terms = 10
fibonacci_list = [1, 1]
for i in range(2, num_terms):
    next_term = fibonacci_list[i - 1] + fibonacci_list[i - 2]
    fibonacci_list.append(next_term)
even_sum = 0
for num in fibonacci_list:
    if num % 2 == 0:
        even_sum += num
print("Fibonacci sequence:", fibonacci_list)
print("Sum of even-valued terms:", even_sum)
