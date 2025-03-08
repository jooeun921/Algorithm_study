import sys
readline = sys.stdin.readline
output = sys.stdout.write

N = int(readline().strip())
xy_plane = [list(map(str, readline().split())) for _ in range(N)]
xy_plane = sorted(xy_plane, key=lambda x:(int(x[0]), int(x[1])))

for line in xy_plane:
    output(" ".join(line) + '\n')