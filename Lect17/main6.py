def generate_add(a:int):
    return lambda x: a + x 


q = generate_add
add10 = q(10)
print("Add10 and 2", add10(2))

