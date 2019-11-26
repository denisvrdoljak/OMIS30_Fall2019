import sys

with open("headers.txt") as headersfp:
    print(headersfp.readlines()[0])

for line in sys.stdin:
    print(line.strip())
