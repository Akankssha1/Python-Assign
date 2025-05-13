def create_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  
print(triple(5))  
