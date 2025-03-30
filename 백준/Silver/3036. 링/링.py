from sys import stdin
from math import gcd

T = int(stdin.readline())
ring = list(map(int, stdin.readline().split()))

a = ring[0]
for i in range(1, len(ring)):
    b = ring[i]
    div = gcd(a, b)
    if div != -1:
        print(f"{a//div}/{b//div}")
    else:
        print(f"{a}/{b}")