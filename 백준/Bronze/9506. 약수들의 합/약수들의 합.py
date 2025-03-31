from sys import stdin

while True:
    n = int(stdin.readline())
    if n == -1:
        break
    n_div = []
    for i in range(1, n):
        if n % i == 0:
            n_div.append(i)
    if sum(n_div) == n:
        print(f"{n} =", end=' ')
        print(*n_div, sep = " + ")
    else:
        print(f"{n} is NOT perfect.")