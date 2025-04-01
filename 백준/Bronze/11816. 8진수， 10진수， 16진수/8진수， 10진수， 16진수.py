from sys import stdin

N = str(stdin.readline())
if '0x' in N:
    print(int(N[2:], 16))
elif N[0] == '0':
    print(int(N[1:], 8))
else:
    print(N)
