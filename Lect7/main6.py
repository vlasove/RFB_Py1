n = int(input())
answer = 1


if n >= 1:
    for i in range(2, n+1):
        answer *= i     

print(answer)