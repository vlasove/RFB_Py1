summ = 0
start = 0
stop = 101.1
step = 2


for i in range(start, stop , step):
    summ += i
    if summ > 1000:
        break 

print("Sum is:", summ)