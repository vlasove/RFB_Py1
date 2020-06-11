message = "5 4 3 4 5 4 23 43 521  4  4  55 5 5 5  55"
words = message.split()

counter = {}

for word in words:
    if word in counter.keys():
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)