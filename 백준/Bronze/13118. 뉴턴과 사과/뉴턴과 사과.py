from sys import stdin

person = list(map(int, stdin.readline().split()))
x, y, r = map(int, stdin.readline().split())

ans = 0
for i in range(len(person)):
    if person[i] == x:
        ans = i+1

print(ans)