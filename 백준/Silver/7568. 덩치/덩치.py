import sys
readline = sys.stdin.readline
N = int(readline())
person = [list(map(int, readline().split())) for _ in range(N)]
ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks, sep=' ')