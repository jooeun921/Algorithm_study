a = int(input())
li = input().strip()
ans = sum(int(li[i]) for i in range(a))
print(ans)