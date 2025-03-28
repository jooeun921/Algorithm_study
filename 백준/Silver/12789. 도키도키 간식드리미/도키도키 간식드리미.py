from sys import stdin
from collections import deque

def can_snake(students):
    queue = deque(students)
    stack = []
    number = 1

    while queue or stack:
        if queue and queue[0] == number:
            queue.popleft()
            number += 1
        elif stack and stack[-1] == number:
            stack.pop()
            number += 1
        elif queue:
            stack.append(queue.popleft())
        else:
            return "Sad"
    return "Nice"

n = stdin.readline()
students = list(map(int, stdin.readline().split()))

print(can_snake(students))