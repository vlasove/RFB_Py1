# with open("data.txt", "r") as fhand:
#     fhand.read()



#Блок с количеством >= 10000 еще не готов. Не трогайте плиз!!
def commission(money:int):
    if money < 10000:
        return 0.01 * money 
    else:
        raise Exception("код еще не готов. Не надо его использовать")
    
