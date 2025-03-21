from sys import stdin
N, M = map(int, input().split())
save_pw = {key: value for key, value in (stdin.readline().split() for _ in range(N))}

for i in range(M):
    find = stdin.readline().strip()
    print(save_pw[find])