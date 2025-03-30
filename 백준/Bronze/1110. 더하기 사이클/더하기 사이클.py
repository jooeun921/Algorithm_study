from sys import stdin

def 사이클찾기(N):
    cycle = 0
    N_now = N
    while True:
        head = N_now % 10
        tail = (N_now // 10 + N_now % 10) % 10
        N_now = head * 10 + tail
        cycle += 1
        if N_now == N:
            break
    return cycle

N = int(stdin.readline().strip())

if N < 10:
    N = N * 10

ans = 사이클찾기(N)
print(ans)