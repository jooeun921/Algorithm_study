dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                dp[a][b][c] = 1
            else:
                if a < b and b < c:
                    dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
                else:
                    dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while True:
    one, two, three = map(int, input().split())
    if one == -1 and two == -1 and three == -1:
        break
    
    if one <= 0 or two <= 0 or three <= 0:
        print(f"w({one}, {two}, {three}) = 1")
    else:
        if one > 20 or two > 20 or three > 20:
            print(f"w({one}, {two}, {three}) = {dp[20][20][20]}")
        else:
            print(f"w({one}, {two}, {three}) = {dp[one][two][three]}")
