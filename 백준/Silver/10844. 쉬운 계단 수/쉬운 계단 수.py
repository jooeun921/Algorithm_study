from sys import stdin

MOD = 1000000000
N = int(stdin.readline())
DP = [[0]* 10 for _ in range(N+1)]

for j in range(1, 10):
    DP[1][j] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][1]
        elif j == 9:
            DP[i][j] = DP[i-1][8]
        else:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % MOD
print(sum(DP[N]) % MOD)