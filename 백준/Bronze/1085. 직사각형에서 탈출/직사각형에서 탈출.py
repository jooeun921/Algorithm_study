from sys import stdin

x, y, w, h = map(int, stdin.readline().split())

print(min(abs(w-x), abs(h-y), x, y))