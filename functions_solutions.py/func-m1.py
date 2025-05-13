def calculate_total(*nums,discount=0):
    total=sum(nums)
    discount=(discount/100)*total
    return total,discount
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, discount=10))

