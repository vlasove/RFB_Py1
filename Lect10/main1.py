total = set()

n = int(input())
for i in range(n):
    m = int(input())
    students = set() # студенты присутств в i-ый день
    for _ in range(m):
        students.add(input())
    if i == 0:
        total = total.union(students)
    else:
        total = total.intersection(students)

print(len(total))