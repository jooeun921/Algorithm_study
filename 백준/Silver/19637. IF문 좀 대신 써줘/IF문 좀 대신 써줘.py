from sys import stdin
from bisect import bisect_left

n, m = map(int, stdin.readline().split())
n_list = [list(stdin.readline().strip().split()) for _ in range(n)]
m_list = [int(stdin.readline()) for _ in range(m)]
n_num_list = list(int(n_list[i][1]) for i in range(n))

for i in range(m):
    idx = bisect_left(n_num_list, m_list[i])
    print(n_list[idx][0])