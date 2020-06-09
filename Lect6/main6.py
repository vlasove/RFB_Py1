max_value = -100
min_value = 1000000000000


while True:
    num = int(input())
    if num <0 :
        break 

    if num > max_value:
        max_value = num 

    if num < min_value:
        min_value = num

print("Max value is:", max_value)
print("Min value is:", min_value)
