import sys
from bisect import bisect_left

def LIS(arr):
    sub = []
    dp = [0] * len(arr)

    for i, num in enumerate(arr):
        pos = bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
        dp[i] = pos + 1
    return dp

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp1 = LIS(A)
dp2 = LIS(A[::-1])[::-1]

max_length = max(dp1[i] + dp2[i] - 1 for i in range(N))
print(max_length)