from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    count = sum(str(num).count('0') for num in range(N, M + 1))
    print(count)