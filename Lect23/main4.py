def gen(files:list):
    for file in files:
        yield open(file ,"r")

def liner(file):
    for fname in file:
        for line in fname:
            yield line.strip()
        fname.close()
          
files = ["input.txt","input2.txt"]

print(liner(gen(files)).__sizeof__())

for l in liner(gen(files)):
    print(l)


