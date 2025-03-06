N, M = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            card_sum = card[a] + card[b] + card[c]
            if card_sum <= M:
                max_sum = max(max_sum, card_sum)

print(max_sum)