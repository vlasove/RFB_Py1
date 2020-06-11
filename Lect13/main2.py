a_list = [23,50,23]
#a_list.clear()
#print(dir(a_list))
print("23 in ", a_list, "is", a_list.count(23))
print("24 in ", a_list, "is", a_list.count(24))

print("index of 23 is ", a_list.index(23))
a_list.insert(1, 100)
print('After insert:', a_list)
a_list.remove(100) # delete by value
print("After removing:", a_list)

del a_list[0]
print(a_list)


