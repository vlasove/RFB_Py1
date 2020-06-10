serials = set()
n = int(input()) # сколько сериалов в библиотеке
m = int(input()) # сколько будем искать

#заполняем библиотеку
for _ in range(n):
    serials.add(input())

for _ in range(m):
    current_serial = input()
    if current_serial in serials:
        print("ЕСТЬ")
    else:
        print("НЕТ В НАЛИЧИИ")


A_set = set()
B_set = set()

new_set = A_set.intersection(B_set) # пересечение множеств
new_set = A_set.union(B_set) # объединение множеств