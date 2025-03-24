from sys import stdin
from bisect import bisect_left

input = stdin.readline
N = int(input())
input_list = list(map(int, input().split()))

lis = []
lis_dic = {}
lis_index = []

for i in range(N):
    num = input_list[i]
    idx = bisect_left(lis, num)
    if idx == 0:
        lis_dic[i] = None
    else:
        lis_dic[i] = lis_index[idx - 1]

    if len(lis) == idx:
        lis.append(num)
        lis_index.append(i)
    else:
        lis[idx] = num
        lis_index[idx] = i

last = lis_index[-1]
ans = []
while last is not None:
    ans.append(input_list[last])
    last = lis_dic[last]

print(len(lis))
print(*ans[::-1])