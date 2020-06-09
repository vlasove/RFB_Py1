a_set = set([1,2,3,4,5])
b_set = set([4,5,6,7,8])

c_set = a_set.intersection(b_set)
print("Intersection:", c_set)
d_set = a_set.union(b_set)
print("Union:", d_set)

e_set = b_set - a_set # a_set.difference(b_set)
print("Difference:", e_set)

f_set = a_set.symmetric_difference(b_set)
print("Symmetric difference:", f_set)