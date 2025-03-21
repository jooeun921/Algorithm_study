from sys import stdin

N = int(input())
log = stdin.readline().strip()
stack = []

success = 1

for char in log:
    if char.islower():
        stack.append(char)
    else:
        if not stack or stack[-1] != char.lower():
            success = 0
            break
        stack.pop()

if stack:
    success = 0

print(success)