from sys import stdin

while True:
    n = int(stdin.readline())
    if n == -1:
        break

    ans = []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)
    
    if sum(ans) ==  n:
        print(f"{n} = ", end='')
        print(*ans, sep=' + ')
    else:
        print(f"{n} is NOT perfect.")
    