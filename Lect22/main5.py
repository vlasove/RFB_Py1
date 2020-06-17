import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="first X argument in expression", type=int)
parser.add_argument("y", help="second Y argument in expression", type=int)
parser.add_argument("-e","--expression", help='if exists - show (x ^ y), if not - (x + y)', action="store_true")

args = parser.parse_args()

if args.expression:
    print("The power operation:", args.x ** args.y)
else:
    print("The sum operation:", args.x + args.y)