import sys
readline = sys.stdin.readline
a, b = map(str, readline().strip().split())
a_re = a[::-1]
b_re = b[::-1]

if int(b_re) > int(a_re):
    print(b_re)
else:
    print(a_re)