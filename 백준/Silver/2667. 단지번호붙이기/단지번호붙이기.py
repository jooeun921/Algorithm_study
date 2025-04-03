from sys import stdin

N = int(stdin.readline().strip())
grid = [list(map(int, stdin.readline().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    grid[x][y] = 0
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                stack.append((nx, ny))
                count += 1

    return count

complex_list = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            complex_list.append(dfs(i, j))

complex_list.sort()
print(len(complex_list))
print(*complex_list, sep='\n')
