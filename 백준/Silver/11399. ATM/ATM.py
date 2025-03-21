N = int(input())
time_list = sorted(list(map(int, input().split())))
time = 0
for i in range(N):
    time += sum(time_list[:i+1])
print(time)