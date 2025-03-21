from sys import stdin

N, M = map(int, stdin.readline().split())

듣보잡 = []

듣도못한 = set(stdin.readline().strip() for _ in range(N))
보도못한 = set(stdin.readline().strip() for _ in range(M))

듣보잡 = sorted(듣도못한 & 보도못한)

print(len(듣보잡), *듣보잡, sep="\n")