import sys
import argparse


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


commands = {"add": add, "sub": sub}

command = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

print(sys.argv)
print(commands[command](x, y))
