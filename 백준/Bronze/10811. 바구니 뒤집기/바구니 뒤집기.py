m, n = map(int, input().split())
bag = [a for a in range(1, m+1)]

for _ in range(n):
    i, j = map(int, input().split())
    bag[i-1:j] = reversed(bag[i-1:j])
print(*bag)