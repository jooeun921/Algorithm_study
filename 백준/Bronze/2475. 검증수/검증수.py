n = list(map(int, input().split()))
ans = 0
for i in range(len(n)):
    ans += n[i]**2
print(ans%10)