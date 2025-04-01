from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    a, b = map(str, stdin.readline().split())
    if a == b :
        print("OK")
    else:
        print("ERROR")