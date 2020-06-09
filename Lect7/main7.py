n = int(input())
summ = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        summ += num 
    else:
        summ -= num 

print(summ)

