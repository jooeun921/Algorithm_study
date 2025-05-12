from sys import stdin

N, L = map(int, stdin.readline().split())

found = False
for length in range(L, 101):
    numerator = 2*N - length*(length-1)
    if numerator % (2*length) == 0:
        a = numerator//(2*length)
        if a >=0:
            result = [a+i for i in range(length)]
            print(*result, sep=' ')
            found = True
            break

if not found:
    print(-1)