from sys import stdin

def backpack(n, k, items):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, k + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
    
    return dp[n][k]

n, k = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for _ in range(n)]

print(backpack(n, k, items))