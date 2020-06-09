summ = 0
while True:
    num = int(input())
    if num <= 0:
        break 

    if num % 2 == 0:
        summ += num  

print("Sum of evens is : ", summ)
print("After while loop")