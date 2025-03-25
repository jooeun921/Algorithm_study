from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

lis = []

for num in seq:
    idx = bisect_left(lis, -num)
    if idx == len(lis):
        lis.append(-num)
    else:
        lis[idx] = -num
print(len(lis))