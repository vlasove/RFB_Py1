def counter(num:int):
    print("Counter started!!")
    i = 0
    while i <= num:
        yield i 
        i += 1 


print(counter(10).__sizeof__())
print([x for x in range(0, 11)].__sizeof__())

# for elem in counter(10):
#     print(elem)


# try:
#     raise TypeError("message")
# except TypeError as t_err:
#     print("type exception happend:", t_err)