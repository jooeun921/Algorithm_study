from sys import stdin
from math import gcd

T = int(stdin.readline())
for _ in range(T):
    ans = 0
    n_list = list(map(int, stdin.readline().split()))
    for i in range(1, len(n_list)-1):
        for j in range(i+1, len(n_list)):
            a, b = n_list[i], n_list[j]
            ans += gcd(a, b)
    print(ans)