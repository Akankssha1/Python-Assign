def merge_sorted_list(num,nums):
    num.sort()
    nums.sort()
    sorted_list=num + nums
    sorted_list.sort()
    return sorted_list
print(merge_sorted_list([1,2,3],[3,4,5]))
print(merge_sorted_list([4,5,6],[5,7]))