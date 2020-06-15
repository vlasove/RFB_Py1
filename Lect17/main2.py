def factorial(n:int):
    if n < 2:
        return 1 
    else:
        return n * factorial( n - 1)

print("5! =",factorial(5))
print("120! =", factorial(120))
print("1200! =", factorial(1200))
    