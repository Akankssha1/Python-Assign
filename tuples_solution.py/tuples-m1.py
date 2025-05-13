from collections import namedtuple
student = namedtuple('student',['name','age','grade'])
def top_student(student):
    topstd=max(student,key=lambda s:sum(s.grade)/len(s.grade))
    return topstd
alice = student("Alice", 20, (85, 90, 95))
bob = student("Bob", 19, (70, 80, 90))
charlie = student("Charlie", 21, (90, 92, 93))
print(top_student([alice, bob, charlie]))

