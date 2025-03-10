import sys

readline = sys.stdin.readline
write = sys.stdout.write
stack = []
N = int(readline().strip())
for i in range(N):
    m = int(readline().strip())
    if m == 0:
        stack.pop()
    else:
        stack.append(m)

write(str(sum(stack)))