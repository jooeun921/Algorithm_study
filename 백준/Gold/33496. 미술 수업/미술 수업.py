from sys import stdin

N = int(stdin.readline())
N_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

diag_plus = set(x - y for x, y in N_list)
diag_minus = set(x + y for x, y in N_list)
meet = diag_plus & diag_minus
example = diag_plus | diag_minus
example -= meet

cnt = 0
diag_plus = list(diag_plus)
diag_minus = list(diag_minus)
for i in range(len(diag_plus)):
    for j in range(len(diag_minus)):
        if diag_plus[i] < diag_minus[j]:
            cnt += 1
print(cnt + len(meet) + len(example))