n = int(input())
li = list(map(int, input().split()))
v = int(input())
ans = 0
for i in range(n):
    if li[i] == v:
        ans += 1
print(ans)