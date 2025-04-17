from sys import stdin

a = stdin.readline()
b = stdin.readline()
print("no" if len(a) < len(b) else "go")
