a, x = map(int, input().split())
li = list(map(int, input().split()))
for i in range(a):
    if li[i] < x:
        print(li[i], end=' ')