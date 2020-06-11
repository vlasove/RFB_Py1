a_set = set([1,2,3,4,5,6,7,8,9])
b_str = "1,2,3,4,5,6,7,8,9"
c_list = [1,2,3,4,5,6,7,8,9]
d_tuple = (1,2,3,4,5,6,7,8,9)
e_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

print("Set:", a_set, "in bytes", a_set.__sizeof__())
print("Str:", b_str, "in bytes", b_str.__sizeof__())
print("List:", c_list, "in bytes", c_list.__sizeof__())
print("Tuple:", d_tuple, "in bytes", d_tuple.__sizeof__())
print("Dict:", e_dict, "in bytes", e_dict.__sizeof__())
