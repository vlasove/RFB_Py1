import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output text", action="store_true")
args = parser.parse_args()

print(args)
if args.verbosity:
    print("First line")
    print('Second line')
else:
    print("line")