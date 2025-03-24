from sys import stdin
from bisect import bisect_left

N = int(stdin.readline().strip())
input_list = stdin.readline().strip().split()

DP = []

for i in range(N):
    idx = bisect_left(DP, int(input_list[i]))
    if idx == len(DP):
        DP.append(int(input_list[i]))
    else:
        DP[idx] = int(input_list[i])

print(len(DP))