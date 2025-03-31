from sys import stdin

N, D, K = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))
state = [0] * N
clean = 0

for _ in range(D):
    for i in range(N):
        if state[i] + s[i] > K:
            clean += 1
            state = [0] * N
    for i in range(N):
        state[i] += s[i]

print(clean)
