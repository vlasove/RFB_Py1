r = range(1,20)
print(type(r))
print(len(r))
print(r.__sizeof__())
nums = [x for x in range(1,20)]
print("List size:", nums.__sizeof__())