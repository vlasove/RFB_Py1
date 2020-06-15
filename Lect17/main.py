def my_func(a:int, b:int): 
    result = a**2 + b**3
    #print("Yes")
    return result 
    


def sqrt_add(a:float = 1, b:float = 1, c:float = 0):
    return (a + b + c) ** ( 0.5)


res = my_func(2,3)
print("Result:", res)

#res1 = my_func(3)
#res1 = my_func(3,4,5)

print("Res1:", sqrt_add(3,2,1))
print("Res2:", sqrt_add(3,2))
print("Res3:", sqrt_add(3))
print("Res4:", sqrt_add())