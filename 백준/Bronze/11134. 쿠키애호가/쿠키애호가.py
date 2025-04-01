from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n, c = map(int, stdin.readline().split())
    day = n // c
    print(day if n%c == 0 else day +1)