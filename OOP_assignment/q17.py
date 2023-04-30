# WAP that has a class numbers with values stored in the list. Write a class method to find the largest value. 

class Numbers:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list
    
    def find_largest(cls, numbers_list):
        largest_num = max(numbers_list)
        return largest_num

numbers = Numbers([5, 10, 15, 20])
largest_num = Numbers.find_largest(numbers.numbers_list)
print(largest_num) 
