from sys import stdin

map_99 = [list(stdin.readline().strip().split()) for _ in range(9)]
max_num = 0
save_i = 0
state = 0
for i in range(9):
    max_num_now = int(max(map_99[i]))
    if max_num_now > max_num:
        max_num = max_num_now
        state = map_99[i].index(str(max_num))    
        save_i = i
print(max_num)
print(save_i+1, state+1)