chess = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))
new = (chess[i]-find[i] for i in range(6))
print(*new)