# a_list = [ "a", "b", "c"]
# print(a_list[-1])
# print(a_list[:2])


# a_list[0] = "A"
# print(a_list)

a_list = [ "a", "b", "c"]
b_list = a_list[:] #a_list.copy() 

b_list[0] = "KEK"

print("After:", a_list)
print("After:", b_list)