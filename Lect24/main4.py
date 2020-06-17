def my_decorator(fn):
    def wrapper():
        print("I'm code before function")
        fn()
        print("I'm code after function")
    return wrapper 


# regular_function = my_decorator(regular_function)
# 

@my_decorator
def regular_function():
    print("!!!!I'm simple regular function!!!!")


@my_decorator
def regular2():
    print( "")

regular_function()
print()
regular2()