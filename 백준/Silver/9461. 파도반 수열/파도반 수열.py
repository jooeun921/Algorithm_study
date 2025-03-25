from sys import stdin

N = int(stdin.readline())
DP = [0, 1, 1, 1, 2, 2, 3, 4, 5]

for i in range(0, 92):
    DP.append(DP[4 + i] + DP[-1])

for _ in range(N):
    print(DP[int(stdin.readline())])