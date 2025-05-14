from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    answer = 0
    for _ in range(N):
        answer += int(stdin.readline())
    if answer > 0:
        print("+")
    elif answer == 0:
        print(0)
    else:
        print("-")