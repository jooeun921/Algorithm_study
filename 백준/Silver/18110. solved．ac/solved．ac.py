import sys

N = int(sys.stdin.readline().strip())
if N == 0:
    print(0)
else:
    diff = [int(sys.stdin.readline().strip()) for _ in range(N)]
    cut = int(N * 0.15) if (N * 0.15) - int(N * 0.15) < 0.5 else int(N * 0.15 + 1)
    diff.sort()
    a = diff[cut:N-cut] if cut > 0 else diff
    avg = sum(a) / len(a)
    print(int(avg) if avg - int(avg) < 0.5 else int(avg + 1))