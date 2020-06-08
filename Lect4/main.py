#if expression:
#  body

a_int = 20
b_int = 30


print(a_int > b_int) # <, >=, <=

print( a_int == b_int) # !=

print( 0 == 0.0)


age = int(input())

if age >= 18 and age < 31:
    print("WELCOME!")


name = "Derek Von Grass"
if "Von" in name:
    print("Dutch guy")


if 30 % 2 == 0:
    print("even")