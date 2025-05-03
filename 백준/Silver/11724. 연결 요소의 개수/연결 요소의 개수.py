import sys
from sys import stdin
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)