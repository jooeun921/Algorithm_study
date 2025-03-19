from sys import stdin
s = 0b0
input = stdin.readline

for _ in range(int(input())):
    op, *e = input().split()
    if e:
        e = int(e[0])-1
        if op=='check': print(1 if s & (1 << e) else 0)
        elif op=='add': s |= 1 << e
        elif op=='remove': s &= ~(1 << e)
        elif op=='toggle': s ^= 1 << e
    else:
        if op=='all': s = 0b11111111111111111111
        elif op=='empty': s = 0b0
