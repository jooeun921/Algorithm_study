from sys import stdin

a = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
b = [c[0]-a[2], c[1]//a[1], c[2]-a[0]]
print(*b, sep=' ')