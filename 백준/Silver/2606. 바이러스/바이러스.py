from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

infected = set()
dfs(1, infected)

print(len(infected) - 1)