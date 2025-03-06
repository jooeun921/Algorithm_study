N = int(input())
score = list(map(int, input().split()))
M = max(score)
print(sum(score[i]/M*100 for i in range(N))/N)