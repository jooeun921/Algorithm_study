import sys
readline = sys.stdin.readline
comand = []
stack = []

N = int(readline().strip())
for i in range(N):
    comand = readline().strip().split()
    if comand[0] == 'push':
        stack.append(comand[1])
    elif comand[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif comand[0] == 'size':
        print(len(stack))
    elif comand[0] == 'empty':
        print(0 if stack else 1)
    elif comand[0] == 'top':
        print(stack[-1] if stack else -1)