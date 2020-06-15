# Ax^2 + Bx + C = 0 

def linear(B:float, C:float):
    #Bx + C = 0
    if B == 0 :
        return 0
    else:
        return 1

def quadratic(A:float, B:float, C:float):
    d = B**2 - 4*A*C 
    if d > 0:
        return 2 
    elif d == 0:
        return 1 
    else:
        return 0


def solve(A:float, B:float, C:float):
    if A == 0 :
        return linear(B,C)
    else:
        return quadratic(A,B,C)


print("1x^2 + 10x + 2 = 0 solutions",solve(1,10,2))

print(linear(2,4) == 1)