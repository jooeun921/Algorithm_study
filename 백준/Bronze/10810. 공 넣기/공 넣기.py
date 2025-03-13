n, m = map(int, input().split())
stack = [0] * n

for _ in range(m):
    f, l, num = map(int, input().split())
    stack[f-1:l] = [num] * (l - (f-1))

print(*stack)