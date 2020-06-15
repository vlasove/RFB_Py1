def dangerous(n : int):
    return 1 / n


#Exception block 24
try:
    num = int(input())   
    dangerous(num)
except ZeroDivisionError as z_err:
    print("exception happend: ", z_err)
except ValueError as v_err:
    print("exception happend with value:", v_err)
except KeyboardInterrupt as k_err:
    print("Please, enter value:", k_err)
else:
    print('Exception block 24 was succefull completed by user.....')
finally:
    print("Finally block working")
