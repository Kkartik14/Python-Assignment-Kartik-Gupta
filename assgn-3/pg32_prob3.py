# WAP to find the median of a list of numbers. 

def find_median(nums):
    sorted_nu = sorted(nums)
    n = len(sorted_nu)
    if n % 2 == 0:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (sorted_nu[middle_left] + sorted_nu[middle_right]) / 2
    else:
        middle = n // 2
        median = sorted_nu[middle]
    return median

numbers = [5, 2, 7, 3, 8, 1, 9, 4, 6]
median = find_median(numbers)
print(median)
