from sys import stdin
from collections import Counter

dot_list = [list(map(int, stdin.readline().split())) for _ in range(3)]
dot_list_x = Counter(dot_list[i][0] for i in range(3))
dot_list_y = Counter(dot_list[i][1] for i in range(3))

ans = []

for num in dot_list_x:
    if dot_list_x[num] == 1:
        ans.append(num)
for num in dot_list_y:
    if dot_list_y[num] == 1:
        ans.append(num)

print(*ans)
