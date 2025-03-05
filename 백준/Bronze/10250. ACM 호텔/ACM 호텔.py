import math
T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    if n%h == 0:
        floor = h
    else:
        floor = n%h
    place = '00' + str(math.ceil(n/h))
    print(str(floor) + place[-2:])