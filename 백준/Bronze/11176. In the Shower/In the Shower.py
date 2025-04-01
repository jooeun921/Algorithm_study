from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    a, b = map(int, stdin.readline().split())
    ans = 0
    for i in range(b):
        n = int(stdin.readline())
        if n > a:
            ans += 1
    print(ans)