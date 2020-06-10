to_park = set()
to_home = set()

while True:
    message = input()
    if message == "":
        break 
    to_park.add(int(message))

while True:
    message = input()
    if message == "":
        break 
    to_home.add(int(message))


total = to_park.intersection(to_home)
print(len(total))