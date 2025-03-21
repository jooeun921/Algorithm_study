import sys
N = int(input())
view_cnt = 0
max_height = 0
bar_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
for i in range(1, N+1):
    if bar_list[-i] > max_height:
        max_height = bar_list[-i]
        view_cnt += 1
print(view_cnt)