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

coeffs_list = []
with open("coeffs.txt" , "r") as fhand:
    coeffs_list = [x.strip() for x in fhand.readlines()]

numeric_coeffs_list = []
for coeffs_string in coeffs_list:
    numeric_coeffs_list.append([int(x) for x in coeffs_string.split()]) # [int('2'), int('4'), int('7')]


numeric_answer_list = []
for numeric in numeric_coeffs_list:
    numeric_answer_list.append(str(solve(numeric[0], numeric[1], numeric[2])))

answer = [x + '\n' for x in numeric_answer_list]

with open("answer.txt", "w") as fhand:
    fhand.writelines(answer)