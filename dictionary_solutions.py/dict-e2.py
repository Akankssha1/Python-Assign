def merge_dictionaries(dict1,dict2):
    dict1.update(dict2)
    return dict1
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))