from sys import stdin
from bisect import bisect_left

N = int(stdin.readline().strip())
Ai = list(map(int, stdin.readline().strip().split()))

temp = []

for i in Ai:
    idx = bisect_left(temp, i)
    if idx == len(temp):
        temp.append(i)
    else:
        temp[idx] = i
print(len(temp))