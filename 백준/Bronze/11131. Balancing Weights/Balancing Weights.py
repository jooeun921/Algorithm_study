from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    balance = 0
    for i in range(n):
        balance += 100 * arr[i]
    
    if balance > 0:
        print("Right")
    elif balance < 0:
        print("Left")
    else:
        print("Equilibrium")