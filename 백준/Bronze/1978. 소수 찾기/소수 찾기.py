N = int(input())
num = list(map(int, input().split()))
ans = 0
for i in range(N):
    odd = 0
    for j in range(1, num[i]+1):
        if num[i] % j == 0:
            odd += 1
    if odd == 2:
        ans += 1
print(ans)