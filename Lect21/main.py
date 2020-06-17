

numerator = 0
denominator = 1

for _ in range(3):
    new_numerator = int(input())
    new_denominator = int(input())

    numerator = numerator * new_denominator + new_numerator * denominator 
    denominator = denominator * new_denominator 


print(numerator, "/", denominator)



