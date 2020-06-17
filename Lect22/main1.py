import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="value to be squared" , type=int)
args = parser.parse_args()

print(args)
print(args.square , "is", args.square ** 2, "squared")