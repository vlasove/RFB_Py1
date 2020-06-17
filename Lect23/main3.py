gen = (x * 2 if x % 2 ==0 else x ** 2 for x in range(1000000) )
lst = [x * 2 if x % 2 ==0 else x ** 2 for x in range(1000000)]

print("Generator:", gen.__sizeof__(), "bytes")
print("List:", lst.__sizeof__(), "bytes")