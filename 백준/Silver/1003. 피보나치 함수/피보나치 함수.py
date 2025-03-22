T = int(input())
for _ in range(T):
    a, b = 0, 1
    n = int(input())
    if n == 0 :
        a = 1
        b = 0
    else:
        for _ in range(n-1):
            a, b = b, a + b
    print(a, b)

# 처음 풀이
# def 재귀_횟수(n):
#     fibo = {0:0, 1: 1}
#     if n == 0:
#         zero = 1
#         one = 0
#     else:
#         for i in range(2, n+1):
#             fibo[i] = fibo[i-1] + fibo[i-2]
#         zero = fibo[n-1]
#         one = fibo[n]
#     return zero, one

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     zero, one = 재귀_횟수(n)
#     print(zero, one)