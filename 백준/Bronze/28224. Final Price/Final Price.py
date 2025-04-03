from sys import stdin

T = int(stdin.readline())
T_list = list(int(stdin.readline()) for _ in range(T))
print(sum(T_list))