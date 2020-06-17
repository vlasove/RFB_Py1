import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="the X value", type=int)
parser.add_argument("y", help="the Y value", type=int)

args = parser.parse_args()

print(args)

print(args.x ** args.y)