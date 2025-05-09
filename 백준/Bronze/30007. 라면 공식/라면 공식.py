k = int(input())
for _ in range(k):
    a, b, x = map(int, input().split())
    print(a*(x-1) + b)