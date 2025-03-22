def 재귀_횟수(n):
    memo = {1: 1, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def 동적_횟수(n):
    return n - 2

n = int(input())
print(재귀_횟수(n), 동적_횟수(n))

# 재귀횟수 계산하는 다른 풀이.
# import sys

# input = sys.stdin.readline

# n = int(input())
# a, b = 0, 1
# for _ in range(n):
#     a, b = b, a + b
# print(a, n - 2)