# Set - неупорядочнная (неиндексируемая) коллекция, способная хранить УНИКАЛЬНЫЕ элементы разных типов данных.

a_set = set(["a", "b", "c", "a", "w", "e", "b"])
print(type(a_set), a_set)

a_set.add("Hello")

print(a_set)

empty_set = set()
empty_set.add(5)
empty_set.add(10)
empty_set.add(25)

empty_set.add(None)
empty_set.add("World")

print(empty_set)