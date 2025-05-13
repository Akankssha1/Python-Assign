def calculate_average(*nums):
    if not nums:
        return 0
    num_sum=sum(nums)
    avg=num_sum/len(nums)
    return avg
print(calculate_average(5,10,15,20))
print(calculate_average()) 