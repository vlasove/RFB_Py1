# Кортеж - это индексируемая коллекция, способная хранить элементы РАЗНОГО ТИПА, но при этом не изменяемая.
b_tuple = tuple()
a_tuple = ()


first = (1,2,3)
second = (4,5,6)

print(first + second * 3)

if 2 in first:
    print("YES 2 in", first)

print("Length:", len(first))
print("Sum:", sum(first))
print("Min:", min(first))

for f in first:
    print(f)

