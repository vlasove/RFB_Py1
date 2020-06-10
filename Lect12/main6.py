new_num = [x for x in range(0, 101)]


first = []
for elem in new_num:
    if elem % 2 == 0:
        first.append(elem ** 2)
    else:
        first.append(elem ** 3)
print(first[:10])


print([elem ** 2 if elem % 2 ==0 else elem ** 3 for elem in new_num][:10])