d = {1 : "one", 2 : 'two', 34.5 : "34.5", False : "False", None : "NoneType"}
d_str = {"one" : 1, "two" : 2, "three" : 3}

d_tuple = {(1,2) : ["one", "and", "two"]}
print(d)
print(d[False])
print(d_str)

print(d_tuple, d_tuple[(1,2)])
