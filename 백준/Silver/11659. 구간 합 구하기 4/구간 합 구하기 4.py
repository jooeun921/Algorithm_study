from sys import stdin

N, M = map(int, stdin.readline().split())
N_list = list(map(int, stdin.readline().split()))

누적합 = [0] * (N+1)
for i in range(1, N+1):
    누적합[i] = 누적합[i-1] + N_list[i-1]

for _ in range(M):
    start, end = map(int, stdin.readline().split())
    print(누적합[end] - 누적합[start-1])