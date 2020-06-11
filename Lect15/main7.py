birth = {
    "янв" : [],
    "фев" : [],
    "мар" : [],
    "апр" : [],
    "май" : [],
    "июн" : [],
    "июл" : [],
    "авг" : [],
    "сен" : [],
    "окт" : [],
    "ноя" : [],
    "дек" : []
}

n_friends = int(input())
for _ in range(n_friends):
    command = input().split() # ["Имя", "дата", "месяц"]
    birth[command[-1]].append(command[0])

print(birth)

months = int(input())
for _ in range(months):
    month = input()
    if len(birth[month]) == 0:
        print()
    else:
        print(" ".join(sorted(birth[month])))