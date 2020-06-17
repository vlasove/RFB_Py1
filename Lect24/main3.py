def born_mult(mult:int):
    def borning_mult(a:int):
        return mult * a 

    return borning_mult

mult10 = born_mult(10)
mult3 = born_mult(3)


print(mult10(1), mult10(20), mult10(30))
print(mult3(1), mult3(20), mult3(30))




print(born_mult(10)(20))

#Add(5)(4)(3) ---> 12

def Add(a:int):
    def Add2(b:int):
        def Add3(c:int):
            return a + b + c 
        return Add3 
    return Add2 


print(Add(10)(20)(30))

