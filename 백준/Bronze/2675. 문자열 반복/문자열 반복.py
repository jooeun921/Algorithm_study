n = int(input())
for _ in range(n):
    ans = ''
    a, b = input().split()
    for char in b:
        ans += char * int(a)
    print(ans)