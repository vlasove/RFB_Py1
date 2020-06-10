# Список - упорядоченная (индексируемая) коллекция, способная хранить элементы любого типа
a_list = [1, 2, 3]
b_list = [10, 20, 30] 
d_list = [0] * 100

print(type(b_list), len(b_list), b_list)

c_list = a_list + b_list * 5
print(c_list)

a_list.append(100)
print("A list after .append():", a_list)
popper = a_list.pop()
print("A list after .pop():", a_list, popper)