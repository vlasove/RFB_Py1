import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--x', help="the X value. Default 1", type=int)
parser.add_argument('--y', help="the Y value. Default 1", type=int)

args=parser.parse_args()
print(args)

if (args.x is not None) and (args.y is not None):
    print(args.x ** args.y)

elif (args.x is None) and (args.y is not None):
    print(1 ** args.y)
elif (args.x is not None) and (args.y is None):
    print(args.x ** 1)
else:
    print(1 ** 1)
