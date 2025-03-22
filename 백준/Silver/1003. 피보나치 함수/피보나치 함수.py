T = int(input())
for _ in range(T):
    a, b = 0, 1
    n = int(input())
    if n == 0 :
        a = 1
        b = 0
    else:
        for _ in range(n-1):
            a, b = b, a + b
    print(a, b)