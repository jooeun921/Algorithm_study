from sys import stdin

N = int(stdin.readline())
T = []
P = []
for _ in range(N):
    t, p = map(int, stdin.readline().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+2)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i + T[i-1] - 1 <= N:
        dp[i + T[i-1]] = max(dp[i + T[i-1]], dp[i] + P[i-1])

print(max(dp))
