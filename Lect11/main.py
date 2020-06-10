# Строка - упорядоченная (индексируемая) коллекция, способная хранить элементы только одного типа.
a_str = "Hello world"
string_set = set(["H", "Hello", "W"])

if "Hello" in string_set:
    print("YES")

len(a_str)

if "Hell" in a_str:
    print("Yes")

last_index = len(a_str) - 1

print("First letter:", a_str[0])
print("Second letter:", a_str[1])
print("Last letter:", a_str[len(a_str) - 1])
print("Another last index:", a_str[-1])

for i in range(0, len(a_str), 1):
    print(a_str[i])

for letter in a_str:
    print(letter)