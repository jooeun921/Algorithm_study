from sys import stdin

T = int(stdin.readline())
N = int(stdin.readline())
F = list(map(int, stdin.readline().strip().split()))

print("Padaeng_i Happy" if T <= sum(F) else "Padaeng_i Cry")