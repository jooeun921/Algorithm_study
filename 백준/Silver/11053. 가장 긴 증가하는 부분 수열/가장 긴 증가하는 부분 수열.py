# # DP로 풀기
# from sys import stdin

# N = int(stdin.readline().strip())
# Ai = stdin.readline().strip().split()

# dp = [1] * N

# for i in range(1, N):
#     for j in range(0, i):
#         if int(Ai[i]) > int(Ai[j]):
#             dp[i] = max(int(dp[i]), int(dp[j]+1))
# print(max(dp))

# 이진탐색으로 풀기
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