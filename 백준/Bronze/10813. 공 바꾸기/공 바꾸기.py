N, M = map(int, input().split())
bag = list(i for i in range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    mid = 0
    mid = bag[a-1]
    bag[a-1] = bag[b-1]
    bag[b-1] = mid
print(*bag)