def talk(choise:str):
    def shout(word:str="HERE!"):
        return word.upper()

    def quiet(word:str="here!"):
        return word.lower()
    
    if choise == "shout":
        return shout
    else:
        return quiet


s_shout = talk("shout")
s_quiet = talk("")

print(s_shout("Moscow"))
print(s_quiet("Moscow"))

print(talk("shout")("Moscow"))





