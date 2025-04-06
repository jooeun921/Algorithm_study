from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(sorted, graph))

visited_dfs = [False]*(N+1)
def dfs(graph, idx, visited_dfs):
    visited_dfs[idx] = True
    print(idx, end=' ')
    for i in graph[idx]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

dfs(graph, V, visited_dfs)
print()

visited_bfs = [False]*(N+1)
def bfs(graph, start, visited_bfs):
    bfs_que = deque([start])
    visited_bfs[start] = True
    
    while bfs_que:
        idx = bfs_que.popleft()
        print(idx, end=' ')
        for i in graph[idx]:
            if not visited_bfs[i]:
                bfs_que.append(i)
                visited_bfs[i] = True
        
bfs(graph, V, visited_bfs)


# from sys import stdin
# from collections import deque

# N, M, V = map(int, stdin.readline().split())
# edges = [list(map(int, stdin.readline().split())) for _ in range(M)]
# graph = [[] for _ in range(N+1)]
# for a, b in edges:
#     graph[a].append(b)
#     graph[b].append(a)
# graph = list(map(sorted, graph))

# visited_dfs = [False]*(N+1)
# def dfs(graph, idx, visited_dfs):
#     visited_dfs[idx] = True
#     print(idx, end=' ')
#     for i in graph[idx]:
#         if not visited_dfs[i]:
#             dfs(graph, i, visited_dfs)

# dfs(graph, V, visited_dfs)
# print()

# visited_bfs = [False]*(N+1)
# def bfs(graph, start, visited_bfs):
#     bfs_que = deque([start])
#     visited_bfs[start] = True
    
#     while bfs_que:
#         idx = bfs_que.popleft()
#         print(idx, end=' ')
#         for i in graph[idx]:
#             if not visited_bfs[i]:
#                 bfs_que.append(i)
#                 visited_bfs[i] = True
        
# bfs(graph, V, visited_bfs)