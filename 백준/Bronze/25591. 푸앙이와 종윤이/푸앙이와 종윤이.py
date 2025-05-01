from sys import stdin

n1, n2 = map(int, stdin.readline().split())

a = 100-n1
b = 100-n2
c = 100 - (a+b)
d = a*b

q = d//100
r = d%100
front = c + q

print(a, b, c, d, q, r)
print(front, r)