from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    decimal = str(stdin.readline())
    print(int(decimal, 2))