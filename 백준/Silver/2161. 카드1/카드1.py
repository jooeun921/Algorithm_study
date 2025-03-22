from collections import deque
N = int(input())
card_que = deque(range(1, N+1, 1))
ans = []

while True:
    ans.append(card_que.popleft())
    if len(card_que) == 0:
        break
    card_que.rotate(-1)

print(*ans)