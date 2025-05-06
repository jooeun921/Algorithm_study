from sys import stdin

ans = 0
while True:
    a = int(stdin.readline())
    if a == -1:
        break
    else:
        ans += a

print(ans)