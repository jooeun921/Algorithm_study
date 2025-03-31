from sys import stdin
import math

def 에라토스체(n):
    n_list = [True] * (n+1)
    n_list[0] = False
    n_list[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i+i, n+1, i):
            n_list[j] = False
    return n_list

a = int(stdin.readline())
b = int(stdin.readline())

b_list = 에라토스체(b)

ans_sum = []
for i in range(a, b+1):
    if b_list[i]:
        ans_sum.append(i)

print(f"{sum(ans_sum)}\n{ans_sum[0]}" if len(ans_sum) != 0 else -1)
