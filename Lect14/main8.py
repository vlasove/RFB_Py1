a_set = set([1,2,3,4,5])
a_list = list(a_set)
for i in range(0, len(a_list)):
    if a_list[i] % 2 == 0:
        a_list[i] += 9

a_set = set(a_list)
print(a_set)


a_str = "Hello"
print(list(a_str))