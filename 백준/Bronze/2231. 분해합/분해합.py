N = int(input())
for abc in range(1, N):
    if abc + sum(map(int, str(abc))) == N:
        print(abc)
        break
else:
    print(0)