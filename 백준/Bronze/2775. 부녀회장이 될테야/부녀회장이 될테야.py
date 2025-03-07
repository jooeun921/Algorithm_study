T = int(input())
for _ in range(T):
    k, n = int(input()), int(input())
    apt = [[i for i in range(1, n+1)]]
    for floor in range(1, k+1):
        new_floor = [sum(apt[floor - 1][:i]) for i in range(1, n+1)]
        apt.append(new_floor)

    print(apt[k][n-1])