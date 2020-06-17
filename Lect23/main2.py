letters = ["a", "b", "c", "d"]
gen = (x for x in letters)

def gen2(letters):
    for let in letters:
        yield let 


for elem in gen2(letters):
    print(elem)

print(gen, gen2(letters))
#print(next(gen))
print(type(gen), type(gen2(letters)))