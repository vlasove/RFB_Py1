# Ax^2 + Bx + C = 0
# 0 0 1
# 0 1 0
# 1 0 0


A = float(input())
B = float(input())
C = float(input())

if A == 0:
    #Bx + C = 0
    # x = -C / B
    if B!= 0:
        print("один корень")
    else:
        print("корней нет")
else:
    d = B**2 - 4*A*C  
    if d > 0 :
        print("два корня")
    elif d == 0:
        print("один корень")
    else:
        print("корней нет")