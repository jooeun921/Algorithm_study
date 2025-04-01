from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    A, B = map(int, stdin.readline().split())
    k = A // B
    print(k * k)