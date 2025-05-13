def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

n = int(input())
my_list = [i for i in range(n)]
print(calculate_average(my_list))

