N = int(input())
plan = list(map(int, input().split()))
real = list(map(int, input().split()))
day = 0
for i in range(N):
    if plan[i] <= real[i]:
        day += 1
print(day)