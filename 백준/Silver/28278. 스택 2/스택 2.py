from sys import stdin
N = int(stdin.readline().strip())
stack=[]
for _ in range(N):
    명령 = stdin.readline().strip().split()
    if 명령[0] == '1':
        stack.append(int(명령[1]))
    if 명령[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if 명령[0] == '3':
        print(len(stack))
    if 명령[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if 명령[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])