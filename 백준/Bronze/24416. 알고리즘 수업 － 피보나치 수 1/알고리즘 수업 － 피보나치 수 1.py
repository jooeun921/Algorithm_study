def 재귀_횟수(n):
    memo = {1: 1, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def 동적_횟수(n):
    return n - 2

n = int(input())
print(재귀_횟수(n), 동적_횟수(n))