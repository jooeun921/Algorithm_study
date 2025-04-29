from sys import stdin

a, b, c = map(int, stdin.readline().split())
print(a+c if a+c > b else b)