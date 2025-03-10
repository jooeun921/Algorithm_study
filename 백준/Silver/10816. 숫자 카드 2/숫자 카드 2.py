import sys
readline = sys.stdin.readline

N = int(readline().strip())
N_list = list(map(str, readline().strip().split()))
M = int(readline().strip())
M_list = list(map(str, readline().strip().split()))

count_dict = {}

for n in N_list:
    if n in count_dict:
        count_dict[n] += 1
    else:
        count_dict[n] = 1

print(' '.join(str(count_dict.get(m, 0)) for m in M_list))