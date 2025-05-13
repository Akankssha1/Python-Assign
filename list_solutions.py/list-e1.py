def filter_even_numbers(nums):
    
    even = [i for i in nums if i%2==0]
    return even
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  
print(filter_even_numbers([1, 3, 5]))  
