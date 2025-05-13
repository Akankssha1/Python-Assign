def get_stats(nums):
    min_nums=min(nums)
    max_nums=max(nums)
    sum_nums=sum(nums)
    avg_nums=sum_nums/ len(nums) if len(nums)>0 else 0
    result = (min_nums, max_nums, sum_nums, avg_nums)
    return result
print(get_stats([1, 2, 3, 4, 5]))