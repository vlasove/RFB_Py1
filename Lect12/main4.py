a_list = []
for i in range(0, 11,2):
    a_list.append(i)

for j in range(0, len(a_list)):
    print(a_list[j])

for elem in a_list:
    elem = 200

print(a_list)