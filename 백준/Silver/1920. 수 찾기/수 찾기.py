import sys
readline = sys.stdin.readline

N = int(readline().strip())
A = set(readline().strip().split())
M = int(readline().strip())
M_list = list(readline().strip().split())

for i in range(M):
    if M_list[i] in A:
        print(1)
    else:
        print(0)