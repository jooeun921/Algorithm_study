import sys
readline = sys.stdin.readline
comand = []
que = []

N = int(readline().strip())
for _ in range(N):
    comand = readline().strip().split()
    if comand[0] == 'push':
        que.append(comand[1])
    elif comand[0] == 'pop':
        print(que.pop(0) if que else -1)
    elif comand[0] == 'size':
        print(len(que))
    elif comand[0] == 'empty':
        print(0 if que else 1)
    elif comand[0] == 'front':
        print(que[0] if que else -1)
    elif comand[0] == 'back':
        print(que[-1] if que else -1)