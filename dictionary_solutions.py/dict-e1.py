def invert_dictionary(dict):
    swapped = {v: k for k, v in dict.items()}
    return swapped
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))
