import sys
readline = sys.stdin.readline
T = int(readline().strip())

for _ in range(T):
    line = readline().rstrip()
    stack = []
    VPS = "YES"
    for char in line:
        if char in '(':
            stack.append(char)
        elif char in ')':
            if not stack or stack[-1] != '(':
                VPS = "NO"
                break
            stack.pop()

    if stack:
        VPS = "NO"
    print(VPS)