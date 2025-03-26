from sys import stdin

n = int(stdin.readline())
N = list(map(int, stdin.readline().split()))

max_sum = N[0]
current_sum = N[0]

for i in range(1, n):
    current_sum = max(N[i], current_sum + N[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)