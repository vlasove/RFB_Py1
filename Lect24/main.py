def scream(word:str= "HERE!"):
    return word.upper()

def starter(fn):
    print(fn())

starter(scream)

q = starter
q(scream)