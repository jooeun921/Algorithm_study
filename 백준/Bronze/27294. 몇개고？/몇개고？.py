from sys import stdin

a, b = map(int, stdin.readline().split())
if 12 <= a <= 16 and b == 0:
    print(320)
else:
    print(280)