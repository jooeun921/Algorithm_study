from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    grid[y][x] = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 1:
                queue.append((nx, ny))
                grid[ny][nx] = 0

T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    grid = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        grid[y][x] = 1

    worm_count = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                bfs(x, y)
                worm_count += 1

    print(worm_count)
