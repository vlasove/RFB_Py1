import argparse

def filer(filename:str):
    with open(filename, "w") as fhand:
        fhand.write(str(args.value))

parser = argparse.ArgumentParser()
parser.add_argument("value", help="value to saving in file", type=int)
parser.add_argument("-p", "--path", help="path to file")
args = parser.parse_args()

if args.path is None:
    filename = "data.txt"
else:
    filename = args.path 


filer(filename)