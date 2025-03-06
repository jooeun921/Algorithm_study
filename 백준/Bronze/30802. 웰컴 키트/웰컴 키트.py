import math
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
t_bun = 0
for i in range(6):
    t_bun += math.ceil(size[i] / T)
print(t_bun)
print(N//P, N%P)