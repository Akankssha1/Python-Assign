from collections import Counter
def count_coordinate_occurrences(cords):
    counts=dict(Counter(cords))
    return counts
cords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(cords))