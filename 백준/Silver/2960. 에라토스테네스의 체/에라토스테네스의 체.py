from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
N_list = deque(range(2, N + 1))

count = 0
while N_list:
    p = N_list.popleft()
    count += 1

    if count == K:
        print(p)
        break

    for num in list(N_list):
        if num % p == 0:
            N_list.remove(num)
            count += 1
            if count == K:
                print(num)
                exit()