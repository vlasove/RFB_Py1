

def add(a:int, b:int):
    return a + b 

def sub(a:int, b:int):
    return a - b 

def mult(a:int, b:int):
    return a * b 

def div(a:int, b:int):
    return a / b 

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Sum is : ", add(a, b))