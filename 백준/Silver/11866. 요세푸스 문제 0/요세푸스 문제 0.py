N, K  = map(int, input().split())
N_list = [i for i in range(1, N+1)]
ans = []
state = 0

while len(N_list) != 0:
    state = (state + K - 1) % len(N_list)
    ans.append(N_list.pop(state))
    
print("<" + ", ".join(map(str, ans)) + ">")


# 다른 풀이
# from collections import deque

# N, K = map(int, input().split())
# queue = deque(range(1, N + 1))
# ans = []

# while queue:
#     queue.rotate(-(K - 1))  # K-1번 왼쪽으로 회전 (K번째 사람이 맨 앞에 오도록)
#     ans.append(queue.popleft())  # K번째 사람을 제거하여 정답 리스트에 추가

# print("<" + ", ".join(map(str, ans)) + ">")