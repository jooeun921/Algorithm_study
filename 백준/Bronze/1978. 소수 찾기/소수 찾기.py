# N = int(input())
# num = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#     odd = 0
#     for j in range(1, num[i]+1):
#         if num[i] % j == 0:
#             odd += 1
#     if odd == 2:
#         ans += 1
# print(ans)

# 더 효율적인 답안
N = int(input())
num = list(map(int, input().split()))
ans = 0
import math
for n in num:
    if n == 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1
print(ans)