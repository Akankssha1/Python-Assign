def swap_pairs(nums):
    nums=list(nums)
    for i in range(0,len(nums)-1,2):
        temp=nums[i]
        nums[i]=nums[i+1]
        nums[i+1]=temp
    return tuple(nums)
print(swap_pairs((1,2,3,4)))
print(swap_pairs((1, 2, 3)))


