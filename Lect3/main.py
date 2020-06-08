# Базовые типы данных в Python 
# Integer, Float, String, Boolean, None 

# Integer - int
a_int = 30
b_int = int(input())
# К целому числу возможно привести строку <=> если строки состоит ИСКЛЮЧИТЕЛЬНО из символов ЦИФР ,  а также допускается
# - в самом начале строки

print(type(a_int))

print(a_int + b_int) # *, -
print(a_int / b_int)

print(a_int // b_int) 
print(a_int % b_int)

print(a_int ** 2)

# Floating Point -- float
a_float = 23.123412
b_float = float(input()) # тоже самое, что и к целому + допускается наличие ОДНОЙ точки

print(type(a_float))

print(a_float + b_float) # -, *, /, //, %, **

# Float VS Int
print("F vs Int:", a_int + b_float) # -, *, /, //, %, **


