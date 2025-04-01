import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M = int(sys.stdin.readline())
    min_initial = 0
    current_people = 0

    for _ in range(M):
        P1, P2 = map(int, sys.stdin.readline().split())
        current_people += P1
        current_people -= P2

        if current_people < 0:
            min_initial += abs(current_people)
            current_people = 0

    print(min_initial)
