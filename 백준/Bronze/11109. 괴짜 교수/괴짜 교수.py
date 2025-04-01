from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    d, n, s, p = map(int, stdin.readline().split())
    병렬시간 = d + (n*p)
    직렬시간 = n*s

    if 병렬시간 > 직렬시간:
        print("do not parallelize")
    elif 병렬시간 < 직렬시간:
        print("parallelize")
    else:
        print("does not matter")