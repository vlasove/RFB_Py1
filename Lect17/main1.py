def combo(a:int = 1, b:int = 0, flag:bool = False ):
    result = 0
    if flag:
        result = a ** 2 + b **2 - 2*a*b
    else:
        result = a**2 - b**2 + 2*a*b 

    return result

ans = combo(2,3)
ans2 = combo(2,3, True)
ans3 = combo(b = 10)

print("Res1:", ans)
print("Res2:", ans2)
print("Res3:", ans3)



