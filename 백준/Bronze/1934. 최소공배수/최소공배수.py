from sys import stdin
import math

T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    print(math.lcm(a, b))