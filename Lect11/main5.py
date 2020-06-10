message = "Hello#world"
print(message[0] + message[1] + message[2] + message[3] + message[4])

print(message[0:5:1]) #[start:stop:step=1]
print(message[0:5])

print(message[5:])
print(message[:8])

print(message[::-1])


for elem in message[::-1]:
    print(elem)