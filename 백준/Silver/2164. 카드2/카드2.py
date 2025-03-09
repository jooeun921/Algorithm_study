import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline().strip())
N_deque = deque(range(1, N + 1))

while len(N_deque) > 1:
    N_deque.popleft()
    N_deque.append(N_deque.popleft())
print(*N_deque)
