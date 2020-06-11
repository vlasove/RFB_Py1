d = {1:'one', 2: 'two', 3:'three'}

if 2 in d.keys():
    print("YES")

if "three" in d.values():
    print("YESS!!")

for key in d.keys():
    print(key)

for val in d.values():
    print(val)

for key, val in d.items():
    print(key, val)