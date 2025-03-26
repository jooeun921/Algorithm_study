from sys import stdin

n = int(stdin.readline())
N = set(map(int, stdin.readline().split()))  # 리스트를 집합으로 변경
m = int(stdin.readline())
M = list(map(int, stdin.readline().split()))

for i_m in M:
    print(1 if i_m in N else 0, end=' ')
