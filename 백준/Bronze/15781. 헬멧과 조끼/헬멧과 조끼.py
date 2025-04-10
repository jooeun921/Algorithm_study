from sys import stdin

n, m = map(int, stdin.readline().split())
n_li = list(map(int, stdin.readline().split()))
m_li = list(map(int, stdin.readline().split()))
print(max(n_li) + max(m_li))