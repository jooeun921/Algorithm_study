from sys import stdin

N, K = map(int, stdin.readline().split())
money_list = [int(stdin.readline().strip()) for _ in range(N)]

now_money = K
ans = 0

for coin in reversed(money_list):
    if now_money >= coin:
        cnt = now_money // coin
        now_money -= coin * cnt
        ans += cnt

    if now_money == 0:
        break

print(ans)