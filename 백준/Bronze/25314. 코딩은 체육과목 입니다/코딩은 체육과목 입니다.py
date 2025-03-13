import sys
readline = sys.stdin.readline

n = int(readline().strip())
print("long " * (n//4) + "int")