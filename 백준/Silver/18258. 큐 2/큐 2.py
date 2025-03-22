from sys import stdin
from collections import deque

N = int(stdin.readline())
make_que = deque()
for _ in range(N):
    command = stdin.readline().strip().split()
    if command[0] == "push":
        make_que.append(command[1])
    elif command[0] == "pop":
        print(-1 if len(make_que)==0 else make_que.popleft())
    elif command[0] == "size":
        print(len(make_que))
    elif command[0] == "empty":
        print(1 if len(make_que)==0 else 0)
    elif command[0] == "front":
        print(-1 if len(make_que)==0 else make_que[0])
    elif command[0] == "back":
        print(-1 if len(make_que)==0 else make_que[-1])