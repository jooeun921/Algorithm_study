from collections import deque
N, K = map(int, input().split())
round_que = deque(range(1, N+1, 1))
ans = []

while True:
    round_que.rotate(-(K-1))
    ans.append(round_que.popleft())
    if len(round_que) == 0:
        break

print("<", end="")
print(*ans, sep=", ", end="")
print(">", end="")