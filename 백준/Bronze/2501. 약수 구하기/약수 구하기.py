from sys import stdin

N, K = map(int, stdin.readline().split())
cnt = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        ans = i
        break
    else:
        ans = 0

print(ans)