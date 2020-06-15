import funcs 
#from funcs import add 


# я хочу из пакета calc и модуля foo вытащить функцию foo
from calc.foo import foo
from calc.buzz import buzz
# я хочу импротировать ВЕСЬ модуль foo из пакета calc
#from calc import foo


# from calc import *



print("Add result:", funcs.add(2,3))
foo()
buzz()
