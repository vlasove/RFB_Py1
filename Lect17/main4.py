

def linear(B:float, C:float) -> int:
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

def factorial(n:int):
    if n < 2:
        return 1 
    else:
        return n * factorial( n - 1)

def combo(a:int = 1, b:int = 0, flag:bool = False ):
    result = 0
    if flag:
        result = a ** 2 + b **2 - 2*a*b
    else:
        result = a**2 - b**2 + 2*a*b 

    return result




##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
############################################################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################
##############################

"This function calc my ......"
def simple_add(a:int, b:int):
    return  a**2 + b**3 / (a**2 - b ** 2)

a = 2
b = 3 

lambda_func = lambda a,b: a**2 + b**3 / (a**2 - b ** 2)
c_simple = simple_add(2,3)
c_lambda = lambda_func(2,3)

print(type(c_simple), type(c_lambda))
print(type(lambda_func))
print(type(simple_add))


print((lambda a,b: a**2 + b**3 / (a**2 - b ** 2))(2,3))
print(simple_add)
print(lambda_func)
