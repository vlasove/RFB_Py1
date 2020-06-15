def dangerous(n : int):
    return 1 / n

try:
    num = int(input())   
    dangerous(num)
except ZeroDivisionError as z_err:
    print("exception happend: ", z_err)
except ValueError as v_err:
    print("exception happend with value:", v_err)
except KeyboardInterrupt as k_err:
    print("Please, enter value:", k_err)

file_name = "data.txt"

try:
    with open(file_name, "r") as fhand:
        fhand.read()

except FileNotFoundError as f_err:
    with open(file_name, "w") as fhand:
        fhand.write("")

    with open(file_name, "r") as fhand:
        fhand.read()

except TypeError as t_err:
    print()
    

print("Graceful shutdown!")