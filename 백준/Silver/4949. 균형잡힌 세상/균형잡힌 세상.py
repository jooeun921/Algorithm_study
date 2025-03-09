import sys
readline = sys.stdin.readline

pair = {')' : '(', ']':'['}

while True:
    line = readline().rstrip()
    if line == '.':
        break

    stack=[]
    is_balanced = "yes"

    for char in line:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != pair[char]:
                is_balanced = "no"
                break
            stack.pop()

    if stack:
        is_balanced = "no"
    print(is_balanced)